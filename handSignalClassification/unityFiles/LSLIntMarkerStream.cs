using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using LSL;

public class LSLIntMarkerStream : MonoBehaviour
{
    private const string unique_source_id = "IntBlinkStateStream";
    public string lslStreamName = "Blinky";
    public string lslStreamType = "Markers";
    private liblsl.StreamInfo lslStreamInfo;
    public liblsl.StreamOutlet lslOutlet;
    private int lslChannelCount = 1;
    private double nominal_srate = liblsl.IRREGULAR_RATE;
    private const liblsl.channel_format_t lslChannelFormat = liblsl.channel_format_t.cf_int32;
    private int[] sample;
    // Start is called before the first frame update
    void Start()
    {
        sample = new int[lslChannelCount];

        lslStreamInfo = new liblsl.StreamInfo(
            lslStreamName,
            lslStreamType,
            lslChannelCount,
            nominal_srate,
            lslChannelFormat,
            unique_source_id
        );
        lslOutlet = new liblsl.StreamOutlet(lslStreamInfo);
    }

    public void Write(int marker)
    {
        sample[0] = marker;
        lslOutlet.push_sample(sample);
    }

    public void Write(int marker, double customTimeStamp)
    {
        sample[0] = marker;
        lslOutlet.push_sample(sample, customTimeStamp);
    }

    public void Write(int marker, float customTimeStamp)
    {
        sample[0] = marker;
        lslOutlet.push_sample(sample, customTimeStamp);
    }

    public void WriteBeforeFrameIsDisplayed(int marker)
    {
        StartCoroutine(WriteMarkerAfterImageIsRendered(marker));
    }

    IEnumerator WriteMarkerAfterImageIsRendered(int pendingMarker)
    {
        yield return new WaitForEndOfFrame();
        Write(pendingMarker);
        yield return null;
    }
    // Update is called once per frame
    void Update()
    {
        
    }
}
