using UnityEngine;
using UnityEngine.XR.MagicLeap;
using UnityEngine.UI;
using UnityEngine.Assertions;
using LSL;
using System;

// two options lol:
// 1. have a flag for each marker saying if its repeated or not or something like that
//     and then continuously send out that marker so that it is detected by fixed update
// 2. have display not depend on constant update

public class separateMarkerStream : MonoBehaviour
{
    public Camera Camera;
    public Material NotBlinkingMaterial, BlinkingMaterial;
    public GameObject sphere;
    public LSLIntMarkerStream markerStream;
    MLPrivilegeRequesterBehavior _privilegeRequester;
    private MeshRenderer _meshRenderer;
    private bool blinkingMaterialState;
    private liblsl.StreamInfo[] lslStreamInfo;
    private liblsl.StreamInlet lslInlet;
    private bool streamConnected;
    private bool lastMarkerSnap;
    void Start()
    {
        _privilegeRequester = GetComponent<MLPrivilegeRequesterBehavior>();
        if (_privilegeRequester == null)
        {
            Debug.LogError("Missing Privelege Requester");
            return;
        }
        _privilegeRequester.OnPrivilegesDone += HandlePrivilegesDone;

        Assert.IsNotNull(markerStream, "You forgot to assign the reference to a marker stream implementation!");
        _meshRenderer = sphere.GetComponent<MeshRenderer>();

        blinkingMaterialState = false;
        lastMarkerSnap = false;
        Debug.Log("Magic Leap has been started");
        // while(!checkForStream())
        // {
        //     updateObjectPosition();
        //     continue;
        // }
        checkForStream();
    }

    // Update is called once per frame
    void Update()
    {
        lslInlet = new liblsl.StreamInlet(lslStreamInfo[0]);
        string[] sample = new string[1];
        double result = lslInlet.pull_sample(sample, 0.25f);
        if(Convert.ToDouble(sample[0]) > 0.6)
        {
            if(lastMarkerSnap)
            {
                lastMarkerSnap = false;
            }
            else
            {
                lastMarkerSnap = true;
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
        }
    }

    // working update:
    //         lslInlet = new liblsl.StreamInlet(lslStreamInfo[0]);
    //     string[] sample = new string[1];
    //     double result = lslInlet.pull_sample(sample, 0.25f);
    //     if(Convert.ToDouble(sample[0]) > 0.6)
    //     {
    //         if (!blinkingMaterialState)
    //         {
    //             _meshRenderer.material = BlinkingMaterial;
    //             blinkingMaterialState = true;
    //         }
    //         else
    //         {
    //             _meshRenderer.material = NotBlinkingMaterial;
    //             blinkingMaterialState = false;
    //         }
    //     }

    void FixedUpdate()
    {
            // lslInlet = new liblsl.StreamInlet(lslStreamInfo[0]);
            // string[] sample = new string[1];
            // double result = lslInlet.pull_sample(sample, 0.25f);
            // if(string.Equals(sample[0], "1"))
            // {
            //     if (!blinkingMaterialState)
            //     {
            //         _meshRenderer.material = BlinkingMaterial;
            //         blinkingMaterialState = true;
            //     }
            //     else
            //     {
            //         _meshRenderer.material = NotBlinkingMaterial;
            //         blinkingMaterialState = false;
            //     }
            // }
    }

    private void updateObjectPosition()
    {
    float speed = Time.deltaTime * 5.0f;

    Vector3 pos = Camera.transform.position + Camera.transform.forward;
    sphere.transform.position = Vector3.SlerpUnclamped(sphere.transform.position, pos, speed);

    Quaternion rot = Quaternion.LookRotation(sphere.transform.position - Camera.transform.position);
    sphere.transform.rotation = Quaternion.Slerp(sphere.transform.rotation, rot, speed);
    }

    private bool checkForStream()
    {
        lslStreamInfo = liblsl.resolve_stream("name", "OutStream");
        if(lslStreamInfo.Length > 0){
            return true;}
        else
            return false;
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