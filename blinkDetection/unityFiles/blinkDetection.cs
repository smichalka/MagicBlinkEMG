using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.XR.MagicLeap;
using UnityEngine.UI;
using UnityEngine.Assertions;
using Assets.LSL4Unity.Scripts;

//change gameobject everytime marker is sent in couroutine
//print out what object is being sent
//try to receive markers on magicleap and update gameobject to see it

public class blinkDetection : MonoBehaviour
{
    public Camera Camera;
    public Material NotBlinkingMaterial, BlinkingMaterial;
    public Text ButtonCount, HeadsetCount;
    public LSLIntMarkerStream markerStream;
    public GameObject sphere;
    MLPrivilegeRequesterBehavior _privilegeRequester;
    private bool currentlyBlinking;
    private MeshRenderer _meshRenderer;
    private int counterML;
    private int counterUser;
    private MLInput.Controller _controller;
    private bool blinkingMaterialState;
    private int currentMarker;
    // Start is called before the first frame update
    void Start()
    {
        //Privilege Request Set Up and Implementation
        _privilegeRequester = GetComponent<MLPrivilegeRequesterBehavior>();
        if (_privilegeRequester == null)
        {
            Debug.LogError("Missing Privilege Requester");
            return;
        }
        _privilegeRequester.OnPrivilegesDone += HandlePrivilegesDone;

        //LSL Marker Stream Set Up Check
        Assert.IsNotNull(markerStream, "You forgot to assign the reference to a marker stream implementation!");

        //Set up default variable states for experiment variables.
        currentlyBlinking = false;
        _meshRenderer = sphere.GetComponent<MeshRenderer>();
        blinkingMaterialState = false;
        counterML = 0;
        counterUser = 0;

        //Set up ML 6DOF controller to act as a control to experiment.
        _controller = MLInput.GetController(MLInput.Hand.Left);
        MLInput.OnControllerButtonDown += OnButtonDown;

        //Ensure proper set up
        Debug.Log("Magic Leap has been started");

    }
    // Update is called once per frame
    void Update()
    {
        _meshRenderer = sphere.GetComponent<MeshRenderer>();
        updateObjectPosition();
        Debug.Log("Spam");
        DetectBlink();
        ButtonCount.text = "Button: " + counterUser;
        HeadsetCount.text = "Headset: " + counterML;
    }

    private bool DetectBlink()
    {
        if (MLEyes.LeftEye.IsBlinking && MLEyes.RightEye.IsBlinking)
        {
            if (!currentlyBlinking)
            {
                counterML++;
                markerStream.Write(2);
                currentlyBlinking = true;
                Debug.LogError("Magic Leap has detected a blink, " + counterML + " blinks have been detected");
                if (!blinkingMaterialState)
                {
                    _meshRenderer.material = BlinkingMaterial;
                    blinkingMaterialState = true;
                }
                else
                {
                    _meshRenderer.material = NotBlinkingMaterial;
                    blinkingMaterialState = false;
                }
                return true;
            }
        }
        else
        {
            currentlyBlinking = false;
        }
        return false;
    }
    private void updateObjectPosition()
    {
        float speed = Time.deltaTime * 5.0f;

        Vector3 pos = Camera.transform.position + Camera.transform.forward;
        sphere.transform.position = Vector3.SlerpUnclamped(sphere.transform.position, pos, speed);

        Quaternion rot = Quaternion.LookRotation(sphere.transform.position - Camera.transform.position);
        sphere.transform.rotation = Quaternion.Slerp(sphere.transform.rotation, rot, speed);
    }
    private void OnButtonDown(byte controllerId, MLInput.Controller.Button button) {
        if (button == MLInput.Controller.Button.Bumper)
        {
            counterUser++;
            Debug.Log("User has indicated a blink, " + counterUser + " have now been indicated.");
        }
        if (button == MLInput.Controller.Button.HomeTap)
        {
            counterML = 0;
            counterUser = 0;
        }
    }
    void HandlePrivilegesDone(MLResult result)
    {
        if (!result.IsOk)
        {
            Debug.LogError("Failed to get all requested privileges. MLResult: " + result);
            return;
        }
        Debug.LogError("Privileges Done and Ok");
    }
}
