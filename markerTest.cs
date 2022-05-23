using UnityEngine;
using UnityEngine.XR.MagicLeap;
using UnityEngine.UI;
using UnityEngine.Assertions;

public class markerTest : MonoBehaviour
{
    public Camera Camera;
    public Material NotBlinkingMaterial, BlinkingMaterial;
    // public LSLIntMarkerStream markerStream;
    public GameObject sphere;
    MLPrivilegeRequesterBehavior _privilegeRequester;
    private MeshRenderer _meshRenderer;
    private MLInput.Controller _controller;
    private bool blinkingMaterialState;
    private int count;
    // private liblsl.StreamInfo[] lslStreamInfo;
    // private liblsl.StreamInlet lslInlet;
    // Start is called before the first frame update
    // private bool streamConnected;
    void Start()
    {
        //Privilege Request Set Up and Implementation
        // _privilegeRequester = GetComponent<MLPrivilegeRequesterBehavior>();
        // if (_privilegeRequester == null)
        // {
        //     Debug.LogError("Missing Privilege Requester");
        //     return;
        // }
        // _privilegeRequester.OnPrivilegesDone += HandlePrivilegesDone;

        // //LSL Marker Stream Set Up Check
        // Assert.IsNotNull(markerStream, "You forgot to assign the reference to a marker stream implementation!");

        //Set up default variable states for experiment variables.
        // _meshRenderer = sphere.GetComponent<MeshRenderer>();
        updateObjectPosition();
        blinkingMaterialState = false;

        //Set up ML 6DOF controller to act as a control to experiment.
        _controller = MLInput.GetController(MLInput.Hand.Left);
        MLInput.OnControllerButtonDown += OnButtonDown;

        //Ensure proper set up
        Debug.Log("Magic Leap has been started");

        // streamConnected = checkForStream();
        count = 0;
    }
    // Update is called once per frame
    void Update()
    {
        _meshRenderer = sphere.GetComponent<MeshRenderer>();
        count++;
        if(count<100)
            updateObjectPosition();
    }

    // void FixedUpdate()
    // {
    //     if(streamConnected)
    //     {
    //         lslInlet = new liblsl.StreamInlet(lslStreamInfo[0]);
    //         string[] sample = new string[1];
    //         lslInlet.pull_sample(sample, 0.5);
    //         if(string.Equals(sample[0], "1"))
    //         {
    //             if (!blinkingMaterialState)
    //             {
    //                 _meshRenderer.material = BlinkingMaterial;
    //                 blinkingMaterialState = true;
    //             }
    //             else
    //             {
    //                 _meshRenderer.material = NotBlinkingMaterial;
    //                 blinkingMaterialState = false;
    //             }
    //         }
    //     }
    // }

    // private bool checkForStream()
    // {
    //     lslStreamInfo = liblsl.resolve_stream("name", "MyMarkerStream", 1, 0.5f);
    //     if(lslStreamInfo.Length > 0)
    //         return true;
    //     else
    //         return false;
    // }

    private void updateObjectPosition()
    {
        float speed = Time.deltaTime * 5.0f;

        Vector3 pos = Camera.transform.position + Camera.transform.forward;
        sphere.transform.position = Vector3.SlerpUnclamped(sphere.transform.position, pos, speed);

        Quaternion rot = Quaternion.LookRotation(sphere.transform.position - Camera.transform.position);
        sphere.transform.rotation = Quaternion.Slerp(sphere.transform.rotation, rot, speed);
    }
    private void OnButtonDown(byte controllerId, MLInput.Controller.Button button) {
        updateObjectPosition();
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
    }
    // void HandlePrivilegesDone(MLResult result)
    // {
    //     if (!result.IsOk)
    //     {
    //         Debug.LogError("Failed to get all requested privileges. MLResult: " + result);
    //         return;
    //     }
    //     Debug.LogError("Privileges Done and Ok");
    // }
}
