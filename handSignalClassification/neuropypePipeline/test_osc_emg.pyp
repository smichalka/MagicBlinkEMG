<?xml version='1.0' encoding='utf-8'?>
<scheme description="Neural oscillations indicate various neural activities or neural states, such as, relaxation, emotions, cognitive processing, and motor control. This pipeline provides the core processing required to extract such neural oscillatory patterns in the context of classification between possible categories or scenarios.&#10;&#10;The main node of this pipeline is the Common Spatial Pattern (CSP) filter, which is used to retrieve the components or patterns in the signal that are most suitable to represent desired categories or classes. CSP and its various extensions (available through NeuroPype) provide a powerful tool for building applications based on neural oscillations. Some of the available CSP algorithms in NeuroPype are: CSP and Filterbank CSP which are mostly targeted for classification algorithms and Source Power Comodulation (SPoC) and Filterbank SPoC which are targeted for regression algorithms.&#10;&#10;This pipeline can be divided into 4 main parts, which we discuss in the following:&#10;Data acquisition:&#10;Includes : Import Data (here titled “Import Test Data” and “Import Calibration Data”), LSL input/output, Stream Data and Inject Calibration Data nodes.&#10;In general you can process your data online or offline. For developing and testing purposes you will be mostly performing offline process using a pre-recorded file.&#10;&#10;- The “Import Data” nodes (here titled “Import Test Data” and “Import Calibration Data”) are used to connect the pipeline to files.&#10;&#10;- The “LSL input” and “LSL output” nodes are used to get data stream into the pipeline, or send the data out to the network from the pipeline. (If you are sending markers make sure to check the “send marker” option in “LSL output” node)&#10;&#10;- The “Inject Calibration Data” node is used to pass the initial calibration data into the pipeline before the actual data is processed. The calibration data (Calib Data) is used by adaptive and machine learning algorithms to train and set their parameters initially. The main data is connected to the “Streaming Data” port.&#10;&#10;NOTE regarding “Inject Calibration Data”: &#10;In case you would like to train and test your pipeline using files (without using streaming node), you need to set the “Delay streaming packets” in this node. This enables the “Inject Calibration Data” node to buffer the test data that is pushed into it for one cycle and transfer it to the output port in the next cycle. It should be noted that the first cycle is used to push the calibration data through the pipeline.&#10;&#10;Data preprocess:&#10;Includes: Assign Targets, Select Range,  FIR filter and Segmentation nodes&#10;&#10;- The “Assign Target” node is mostly useful for the supervised learning algorithms, where  target values are assigned to specific markers present in the EEG signal. In order for this node to operate correctly you need to know the label for the markers in the data.&#10;&#10;- The “Select Range” node is used to specify certain parts of the data stream. For example, if we have a headset that contains certain bad channels, you can manually remove them here. That is the case for our example here with data recorded with Cognionics headset that the last 5 channels are not used and are removed.&#10;&#10;- The “FIR Filter” node is used to remove the unwanted signals components outside of the EEG signal frequencies, e.g. to keep the 8-28 Hz frequency window.&#10;&#10;- The “Segmentation” node performs the epoching process, where the streamed data is divided into segments of the predefined window-length around the markers on the EEG data.&#10;&#10;NOTE regarding &quot;Segmentation&quot; node:&#10;The epoching process can be either done relative to the marker or the time window. When Processing a large file you should set the epoching relative to markers and while processing the streaming data, you should set it to sliding which chooses a single window at the end of the data.&#10;&#10;Feature extraction:&#10;&#10;Includes: Filter Bank Common Spatial Patterns (FBCSP) node&#10;As discussed above the spectral and spatial patterns in the data can be extracted by the CSP filters and its extensions. In the FBCSP method, multiple frequency bands can be defined and then desired number of filters are designed for each frequency band. These filters are then applied to the data to extract the features corresponding to model patterns. &#10;You can define the frequency bands of interest for this node. Also, you can choose different windows for frequency calculation in order to avoid the boundary effect.&#10;&#10;Classification:&#10;Includes: Variance, Logarithm, Logistic Regression and Measure Loss&#10;&#10;- The “Logistic Regression” node is used to perform the classification, where supervised learning methods is used to train the classifier. in this node you can choose the type of regularization and the regularization coefficient. You can also set the number of the folds for cross-validation in this node.&#10;&#10;- The “Measure Loss” node is used to measure various performance criteria. For example  you can  use the misclassification rate (MCR) or area under the curve (AUC)." title="Oscillatory process classification" version="2.0">
	<nodes>
		<node id="0" name="FIR Filter" position="(200, 300)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owfirfilter.OWFIRFilter" title="FIR Filter" uuid="98d79c91-0996-4ee1-a2b4-7c3375aeece9" version="1.1.0" />
		<node id="1" name="Segmentation" position="(298.0, 300.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owsegmentation.OWSegmentation" title="Segmentation" uuid="f8a86dac-f39f-43b1-804a-099c9372700e" version="1.0.2" />
		<node id="2" name="Variance" position="(500, 300)" project_name="NeuroPype" qualified_name="widgets.statistics.owvariance.OWVariance" title="Variance" uuid="1be6244d-2f49-4f3e-a734-43458675f577" version="1.0.0" />
		<node id="3" name="Logistic Regression" position="(700, 300)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owlogisticregression.OWLogisticRegression" title="Logistic Regression" uuid="7e764997-fbb3-4ca1-bbcd-8bf4f291697b" version="1.1.0" />
		<node id="4" name="Assign Target Values" position="(500, 100)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owassigntargets.OWAssignTargets" title="Assign Targets" uuid="59c9d795-9879-4b5e-822d-d21df1a7ec84" version="1.0.1" />
		<node id="5" name="Logarithm" position="(600, 300)" project_name="NeuroPype" qualified_name="widgets.elementwise_math.owlogarithm.OWLogarithm" title="Logarithm" uuid="56bb438d-1550-40bb-a2b6-eb22b4601632" version="1.0.0" />
		<node id="6" name="Dejitter Timestamps" position="(200, 100)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="c61aafae-4777-4b41-8104-3eae4ba01ac2" version="1.0.0" />
		<node id="7" name="Select Range" position="(600, 100)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Select Range" uuid="a3c0fbb3-d252-4693-a392-bbe91816ad15" version="1.1.0" />
		<node id="8" name="Inject Calibration Data" position="(400, 100)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owinjectcalibrationdata.OWInjectCalibrationData" title="Inject Calibration Data" uuid="a9e56eff-173f-4703-b66f-6e72b51ce559" version="1.0.0" />
		<node id="9" name="Stream Data" position="(200.0, 499.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data" uuid="7d36ab62-7cb5-4b48-bdae-a28896efa7ad" version="1.2.1" />
		<node id="10" name="LSL Output" position="(300, 500)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="b38757d3-d8c7-4173-a1ec-2d272494b5d4" version="1.4.3" />
		<node id="11" name="LSL Input" position="(101.0, 100.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="f7512141-2966-4108-93c3-2ed872c38346" version="1.3.6" />
		<node id="12" name="LSL Output" position="(901.0, 290.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="463d4338-87cc-44d1-a544-b46552d63c98" version="1.4.3" />
		<node id="13" name="Print To Console" position="(900, 500)" project_name="NeuroPype" qualified_name="widgets.diagnostics.owprinttoconsole.OWPrintToConsole" title="PrintToConsole" uuid="468177f4-911b-42ab-87ba-aa1b0553298d" version="1.1.0" />
		<node id="14" name="Filter Bank Common Spatial Patterns" position="(400, 300)" project_name="NeuroPype" qualified_name="widgets.neural.owfilterbankcommonspatialpattern.OWFilterBankCommonSpatialPattern" title="Filter Bank Common Spatial Patterns" uuid="ead8a35c-bafb-4d87-ad39-bcd9b51088be" version="1.0.0" />
		<node id="15" name="Time Series Plot" position="(800, 600)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot" uuid="c84d73ee-5951-471e-ae82-a2893a41b9bc" version="1.0.3" />
		<node id="16" name="Select Range" position="(600, 600)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Select Range (1)" uuid="0e63393b-5e5d-4219-8537-144c8bbb39f0" version="1.1.0" />
		<node id="17" name="Streaming Bar Plot" position="(1007.0, 160.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owbarplot.OWBarPlot" title="Streaming Bar Plot" uuid="1d6def26-8b14-4401-b8cb-883bdf3e1304" version="1.0.3" />
		<node id="18" name="Override Axis" position="(753.0, 161.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owoverrideaxis.OWOverrideAxis" title="Override Axis" uuid="77a72ff6-8465-4368-a4b3-81afccfcd480" version="1.4.2" />
		<node id="19" name="Mean" position="(856.0, 161.0)" project_name="NeuroPype" qualified_name="widgets.statistics.owmean.OWMean" title="Mean" uuid="fe04ef1a-5678-4ff9-ac4d-e7b9bcf0e495" version="1.0.0" />
		<node id="20" name="Import XDF" position="(227.0, -5.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF (1)" uuid="0e547a28-1407-4a86-b037-1148fe23dc4c" version="1.2.1" />
		<node id="21" name="Import XDF" position="(86.0, 485.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF (2)" uuid="d8dfcc97-a3dd-4a25-bfb9-10392885c091" version="1.2.1" />
		<node id="22" name="Discard Long Chunks" position="(500, 600)" project_name="NeuroPype" qualified_name="widgets.utilities.owdiscardlongchunks.OWDiscardLongChunks" title="Discard Long Chunks" uuid="b7f4ade1-28a9-408a-aa2d-5766c78abc6d" version="1.0.0" />
		<node id="23" name="Inspect Data" position="(128.0, 227.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owinspectdata.OWInspectData" title="Inspect Data" uuid="3bc5a10d-7b1a-4190-813e-fdcb0720b649" version="2.2.4" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="0" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="4" sink_channel="Streaming Data" sink_node_id="8" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="4" source_channel="Data" source_node_id="8" />
		<link enabled="true" id="6" sink_channel="Data" sink_node_id="10" source_channel="Data" source_node_id="9" />
		<link enabled="true" id="7" sink_channel="Data" sink_node_id="6" source_channel="Data" source_node_id="11" />
		<link enabled="true" id="8" sink_channel="Data" sink_node_id="13" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="9" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="14" />
		<link enabled="true" id="10" sink_channel="Data" sink_node_id="18" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="11" sink_channel="Calib Data" sink_node_id="8" source_channel="Data" source_node_id="20" />
		<link enabled="true" id="12" sink_channel="Data" sink_node_id="9" source_channel="Data" source_node_id="21" />
		<link enabled="true" id="13" sink_channel="Data" sink_node_id="16" source_channel="Data" source_node_id="22" />
		<link enabled="true" id="14" sink_channel="Data" sink_node_id="22" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="15" sink_channel="Data" sink_node_id="15" source_channel="Data" source_node_id="16" />
		<link enabled="true" id="16" sink_channel="Data" sink_node_id="12" source_channel="Data" source_node_id="16" />
		<link enabled="true" id="17" sink_channel="Data" sink_node_id="19" source_channel="Data" source_node_id="18" />
		<link enabled="true" id="18" sink_channel="Data" sink_node_id="17" source_channel="Data" source_node_id="19" />
		<link enabled="true" id="19" sink_channel="Data" sink_node_id="23" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="20" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="21" sink_channel="Data" sink_node_id="14" source_channel="Data" source_node_id="1" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWA0AAABhbnRpc3ltbWV0cmljcQGJWAQAAABheGlzcQJYBAAAAHRpbWVxA1gSAAAAY29u
dm9sdXRpb25fbWV0aG9kcQRYCAAAAHN0YW5kYXJkcQVYDgAAAGN1dF9wcmVyaW5naW5ncQaJWAsA
AABmcmVxdWVuY2llc3EHXXEIKEdAAAAAAAAAAEdAEAAAAAAAAEdARQAAAAAAAEdARoAAAAAAAGVY
CAAAAG1ldGFkYXRhcQl9cQpYDQAAAG1pbmltdW1fcGhhc2VxC4hYBAAAAG1vZGVxDFgIAAAAYmFu
ZHBhc3NxDVgFAAAAb3JkZXJxDlgNAAAAKHVzZSBkZWZhdWx0KXEPWBMAAABzYXZlZFdpZGdldEdl
b21ldHJ5cRBjc2lwCl91bnBpY2tsZV90eXBlCnERWAwAAABQeVF0NS5RdENvcmVxElgKAAAAUUJ5
dGVBcnJheXETQ0IB2dDLAAMAAAAAAwsAAAGOAAAEdAAAAlIAAAMMAAABtAAABHMAAAJRAAAAAAAA
AAAHgAAAAwwAAAG0AAAEcwAAAlFxFIVxFYdxFlJxF1gOAAAAc2V0X2JyZWFrcG9pbnRxGIlYCgAA
AHN0b3BfYXR0ZW5xGUdASQAAAAAAAHUu
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWBEAAABrZWVwX21hcmtlcl9jaHVua3EBiVgOAAAAbWF4X2dhcF9sZW5ndGhxAkc/yZmZ
mZmZmlgIAAAAbWV0YWRhdGFxA31xBFgPAAAAb25saW5lX2Vwb2NoaW5ncQVYDQAAAG1hcmtlci1s
b2NrZWRxBlgNAAAAc2FtcGxlX29mZnNldHEHSwBYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxCGNz
aXAKX3VucGlja2xlX3R5cGUKcQlYDAAAAFB5UXQ1LlF0Q29yZXEKWAoAAABRQnl0ZUFycmF5cQtD
QgHZ0MsAAwAAAAADDAAAAYwAAARzAAACeQAAAwwAAAGMAAAEcwAAAnkAAAAAAAAAAAeAAAADDAAA
AYwAAARzAAACeXEMhXENh3EOUnEPWA4AAABzZWxlY3RfbWFya2Vyc3EQWA0AAAAodXNlIGRlZmF1
bHQpcRFYDgAAAHNldF9icmVha3BvaW50cRKJWAsAAAB0aW1lX2JvdW5kc3ETXXEUKEsASwJlWAcA
AAB2ZXJib3NlcRWJdS4=
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgSAAAAZGVncmVlc19vZl9mcmVlZG9tcQNLAFgS
AAAAZm9yY2VfZmVhdHVyZV9heGlzcQSJWAgAAABtZXRhZGF0YXEFfXEGWBMAAABzYXZlZFdpZGdl
dEdlb21ldHJ5cQdjc2lwCl91bnBpY2tsZV90eXBlCnEIWAwAAABQeVF0NS5RdENvcmVxCVgKAAAA
UUJ5dGVBcnJheXEKQ0IB2dDLAAMAAAAAAwsAAAGoAAAEdAAAAjgAAAMMAAABzgAABHMAAAI3AAAA
AAAAAAAHgAAAAwwAAAHOAAAEcwAAAjdxC4VxDIdxDVJxDlgOAAAAc2V0X2JyZWFrcG9pbnRxD4l1
Lg==
</properties>
		<properties format="pickle" node_id="3">gAN9cQAoWAYAAABhbHBoYXNxAV1xAihHP7mZmZmZmZpHP+AAAAAAAABHP/AAAAAAAABLBUdAJAAA
AAAAAGVYDAAAAGJpYXNfc2NhbGluZ3EDRz/wAAAAAAAAWA0AAABjbGFzc193ZWlnaHRzcQRYBAAA
AGF1dG9xBVgKAAAAY29uZF9maWVsZHEGWAsAAABUYXJnZXRWYWx1ZXEHWBAAAABkb250X3Jlc2V0
X21vZGVscQiJWBAAAABkdWFsX2Zvcm11bGF0aW9ucQmJWA8AAABmZWF0dXJlX3NjYWxpbmdxClgE
AAAAbm9uZXELWAwAAABpbmNsdWRlX2JpYXNxDIhYDwAAAGluaXRpYWxpemVfb25jZXENiFgJAAAA
bDFfcmF0aW9zcQ5YDQAAACh1c2UgZGVmYXVsdClxD1gIAAAAbWF4X2l0ZXJxEEtkWAgAAABtZXRh
ZGF0YXERfXESWAoAAABtdWx0aWNsYXNzcRNYAwAAAG92cnEUWAkAAABudW1fZm9sZHNxFUsFWAgA
AABudW1fam9ic3EWSwFYDQAAAHByb2JhYmlsaXN0aWNxF4hYCwAAAHJhbmRvbV9zZWVkcRhNOTBY
CwAAAHJlZ3VsYXJpemVycRlYAgAAAGwycRpYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxG2NzaXAK
X3VucGlja2xlX3R5cGUKcRxYDAAAAFB5UXQ1LlF0Q29yZXEdWAoAAABRQnl0ZUFycmF5cR5DQgHZ
0MsAAwAAAAADCwAAAXIAAAR0AAACbgAAAwwAAAGYAAAEcwAAAm0AAAAAAAAAAAeAAAADDAAAAZgA
AARzAAACbXEfhXEgh3EhUnEiWA0AAABzZWFyY2hfbWV0cmljcSNYCAAAAGFjY3VyYWN5cSRYDgAA
AHNldF9icmVha3BvaW50cSWJWAYAAABzb2x2ZXJxJlgFAAAAbGJmZ3NxJ1gJAAAAdG9sZXJhbmNl
cShHPxo24uscQy1YCQAAAHZlcmJvc2l0eXEpSwB1Lg==
</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWBIAAABhbHNvX2xlZ2FjeV9vdXRwdXRxAYlYDgAAAGlzX2NhdGVnb3JpY2FscQKJWAkA
AABpdl9jb2x1bW5xA1gGAAAATWFya2VycQRYBwAAAG1hcHBpbmdxBX1xBihYAgAAADBzcQdLAFgC
AAAAM3NxCEsBdVgOAAAAbWFwcGluZ19mb3JtYXRxCVgGAAAAY29tcGF0cQpYCAAAAG1ldGFkYXRh
cQt9cQxYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxDWNzaXAKX3VucGlja2xlX3R5cGUKcQ5YDAAA
AFB5UXQ1LlF0Q29yZXEPWAoAAABRQnl0ZUFycmF5cRBDQgHZ0MsAAwAAAAADCwAAAY4AAAR0AAAC
UgAAAwwAAAG0AAAEcwAAAlEAAAAAAAAAAAeAAAADDAAAAbQAAARzAAACUXERhXESh3ETUnEUWA4A
AABzZXRfYnJlYWtwb2ludHEViVgRAAAAc3VwcG9ydF93aWxkY2FyZHNxFolYCwAAAHVzZV9udW1i
ZXJzcReJWAcAAAB2ZXJib3NlcRiJdS4=
</properties>
		<properties format="pickle" node_id="5">gAN9cQAoWAQAAABiYXNlcQFYDQAAACh1c2UgZGVmYXVsdClxAlgIAAAAbWV0YWRhdGFxA31xBFgT
AAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEFY3NpcApfdW5waWNrbGVfdHlwZQpxBlgMAAAAUHlRdDUu
UXRDb3JlcQdYCgAAAFFCeXRlQXJyYXlxCENCAdnQywADAAAAAAMLAAABpwAABHQAAAI5AAADDAAA
Ac0AAARzAAACOAAAAAAAAAAAB4AAAAMMAAABzQAABHMAAAI4cQmFcQqHcQtScQxYDgAAAHNldF9i
cmVha3BvaW50cQ2JdS4=
</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWA8AAABmb3JjZV9tb25vdG9uaWNxAYhYDwAAAGZvcmdldF9oYWxmdGltZXECTSwBWA4A
AABtYXhfdXBkYXRlcmF0ZXEDTfQBWAgAAABtZXRhZGF0YXEEfXEFWBMAAABzYXZlZFdpZGdldEdl
b21ldHJ5cQZjc2lwCl91bnBpY2tsZV90eXBlCnEHWAwAAABQeVF0NS5RdENvcmVxCFgKAAAAUUJ5
dGVBcnJheXEJQwBxCoVxC4dxDFJxDVgOAAAAc2V0X2JyZWFrcG9pbnRxDolYDgAAAHdhcm11cF9z
YW1wbGVzcQ9K/////3Uu
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWB8AAABhcHBseV90aW1lX3NlbGVjdGlv
bl90b19tYXJrZXJzcQKJWAQAAABheGlzcQNYBQAAAHNwYWNlcQRYCAAAAG1ldGFkYXRhcQV9cQZY
EwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxB2NzaXAKX3VucGlja2xlX3R5cGUKcQhYDAAAAFB5UXQ1
LlF0Q29yZXEJWAoAAABRQnl0ZUFycmF5cQpDQgHZ0MsAAwAAAAADCwAAAYEAAAR0AAACXwAAAwwA
AAGnAAAEcwAAAl4AAAAAAAAAAAeAAAADDAAAAacAAARzAAACXnELhXEMh3ENUnEOWAkAAABzZWxl
Y3Rpb25xD1gDAAAAOi02cRBYDgAAAHNldF9icmVha3BvaW50cRGJWAQAAAB1bml0cRJYBwAAAGlu
ZGljZXNxE3Uu
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWBcAAABkZWxheV9zdHJlYW1pbmdfcGFja2V0c3EBiFgIAAAAbWV0YWRhdGFxAn1xA1gT
AAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEEY3NpcApfdW5waWNrbGVfdHlwZQpxBVgMAAAAUHlRdDUu
UXRDb3JlcQZYCgAAAFFCeXRlQXJyYXlxB0MAcQiFcQmHcQpScQtYDgAAAHNldF9icmVha3BvaW50
cQyJdS4=
</properties>
		<properties format="pickle" node_id="9">gAN9cQAoWAoAAABkYXRhX2R0eXBlcQFYBwAAAGZsb2F0NjRxAlgRAAAAaGl0Y2hfcHJvYmFiaWxp
dHlxA0cAAAAAAAAAAFgOAAAAaml0dGVyX3BlcmNlbnRxBEsFWAwAAABsb2dfcHJvZ3Jlc3NxBYlY
BwAAAGxvb3BpbmdxBohYCAAAAG1ldGFkYXRhcQd9cQhYCAAAAHJhbmRzZWVkcQlN54ZYEwAAAHNh
dmVkV2lkZ2V0R2VvbWV0cnlxCmNzaXAKX3VucGlja2xlX3R5cGUKcQtYDAAAAFB5UXQ1LlF0Q29y
ZXEMWAoAAABRQnl0ZUFycmF5cQ1DQgHZ0MsAAwAAAAAC9gAAATwAAASJAAACpAAAAvcAAAFiAAAE
iAAAAqMAAAAAAAAAAAeAAAAC9wAAAWIAAASIAAACo3EOhXEPh3EQUnERWA4AAABzZXRfYnJlYWtw
b2ludHESiVgHAAAAc3BlZWR1cHETRz/wAAAAAAAAWAkAAABzdGFydF9wb3NxFEcAAAAAAAAAAFgQ
AAAAdGltZXN0YW1wX2ppdHRlcnEVRwAAAAAAAAAAWAYAAAB0aW1pbmdxFlgJAAAAd2FsbGNsb2Nr
cRdYDwAAAHVwZGF0ZV9pbnRlcnZhbHEYRz+keuFHrhR7dS4=
</properties>
		<properties format="pickle" node_id="10">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYEwAA
AGtlZXBfc2luZ2xldG9uX2F4ZXNxA4lYDAAAAG1hcmtlcl9maWVsZHEEWAYAAABNYXJrZXJxBVgL
AAAAbWFya2VyX25hbWVxBlgOAAAATXlNYXJrZXJTdHJlYW1xB1gQAAAAbWFya2VyX3NvdXJjZV9p
ZHEIWAAAAABxCVgMAAAAbWF4X2J1ZmZlcmVkcQpLPFgIAAAAbWV0YWRhdGFxC31xDFgXAAAAbnVt
ZXJpY19sYWJlbF9wcmVjaXNpb25xDUsBWBgAAABudW1lcmljX21hcmtlcl9wcmVjaXNpb25xDksD
WBcAAAByZXNldF9pZl9sYWJlbHNfY2hhbmdlZHEPiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEQ
Y3NpcApfdW5waWNrbGVfdHlwZQpxEVgMAAAAUHlRdDUuUXRDb3JlcRJYCgAAAFFCeXRlQXJyYXlx
E0NCAdnQywADAAAAAAMLAAAA0wAABHQAAAMNAAADDAAAAPkAAARzAAADDAAAAAAAAAAAB4AAAAMM
AAAA+QAABHMAAAMMcRSFcRWHcRZScRdYDAAAAHNlbmRfbWFya2Vyc3EYiVgJAAAAc2VwYXJhdG9y
cRlYAQAAAC1xGlgOAAAAc2V0X2JyZWFrcG9pbnRxG4lYCQAAAHNvdXJjZV9pZHEcWA0AAABteXNv
dXJjZWlkMjM0cR1YBQAAAHNyYXRlcR5YDQAAACh1c2UgZGVmYXVsdClxH1gLAAAAc3RyZWFtX25h
bWVxIFgNAAAAT3V0U3RyZWFtRGF0YXEhWAsAAABzdHJlYW1fdHlwZXEiWAMAAABFRUdxI1gTAAAA
dXNlX2RhdGFfdGltZXN0YW1wc3EkiFgWAAAAdXNlX251bXB5X29wdGltaXphdGlvbnEliXUu
</properties>
		<properties format="pickle" node_id="11">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCgAAAGRhdGFfZHR5cGVxA1gHAAAAZmxvYXQ2
NHEEWAsAAABkaWFnbm9zdGljc3EFiVgTAAAAZXhjbHVkZV9kZXNjX2ZpZWxkc3EGXXEHWAwAAABt
YXJrZXJfcXVlcnlxCFgVAAAAbmFtZT0nTXlNYXJrZXJTdHJlYW0ncQlYDAAAAG1heF9ibG9ja2xl
bnEKTQAEWAoAAABtYXhfYnVmbGVucQtLHlgMAAAAbWF4X2NodW5rbGVucQxLAFgIAAAAbWV0YWRh
dGFxDX1xDlgMAAAAbm9taW5hbF9yYXRlcQ9YDQAAACh1c2UgZGVmYXVsdClxEFgJAAAAb21pdF9k
ZXNjcRGJWA8AAABwcmVhbGxvY19idWZmZXJxEohYDgAAAHByb2NfY2xvY2tzeW5jcROIWA0AAABw
cm9jX2Rlaml0dGVycRSJWA8AAABwcm9jX21vbm90b25pemVxFYlYDwAAAHByb2NfdGhyZWFkc2Fm
ZXEWiVgFAAAAcXVlcnlxF1gQAAAAbmFtZT0nb2JjaV9lZWcxJ3EYWAcAAAByZWNvdmVycRmIWBQA
AAByZXNvbHZlX21pbmltdW1fdGltZXEaRz/gAAAAAAAAWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5
cRtjc2lwCl91bnBpY2tsZV90eXBlCnEcWAwAAABQeVF0NS5RdENvcmVxHVgKAAAAUUJ5dGVBcnJh
eXEeQ0IB2dDLAAMAAAAAAwsAAAE3AAAEdAAAAqkAAAMMAAABXQAABHMAAAKoAAAAAAAAAAAHgAAA
AwwAAAFdAAAEcwAAAqhxH4VxIIdxIVJxIlgOAAAAc2V0X2JyZWFrcG9pbnRxI4l1Lg==
</properties>
		<properties format="pickle" node_id="12">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYEwAA
AGtlZXBfc2luZ2xldG9uX2F4ZXNxA4lYDAAAAG1hcmtlcl9maWVsZHEEWAYAAABNYXJrZXJxBVgL
AAAAbWFya2VyX25hbWVxBlgRAAAAT3V0U3RyZWFtLW1hcmtlcnNxB1gQAAAAbWFya2VyX3NvdXJj
ZV9pZHEIWAAAAABxCVgMAAAAbWF4X2J1ZmZlcmVkcQpLPFgIAAAAbWV0YWRhdGFxC31xDFgXAAAA
bnVtZXJpY19sYWJlbF9wcmVjaXNpb25xDUsBWBgAAABudW1lcmljX21hcmtlcl9wcmVjaXNpb25x
DksDWBcAAAByZXNldF9pZl9sYWJlbHNfY2hhbmdlZHEPiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEQY3NpcApfdW5waWNrbGVfdHlwZQpxEVgMAAAAUHlRdDUuUXRDb3JlcRJYCgAAAFFCeXRlQXJy
YXlxE0NCAdnQywADAAAAAAMLAAAA0wAABHQAAAMNAAADDAAAAPkAAARzAAADDAAAAAAAAAAAB4AA
AAMMAAAA+QAABHMAAAMMcRSFcRWHcRZScRdYDAAAAHNlbmRfbWFya2Vyc3EYiFgJAAAAc2VwYXJh
dG9ycRlYAQAAAC1xGlgOAAAAc2V0X2JyZWFrcG9pbnRxG4lYCQAAAHNvdXJjZV9pZHEcWCoAAAAo
bmV2ZXIgdXNlIHNhbWUgc291cmNlIGlkIGluIG9uZSBweXBlbGluZSlxHVgFAAAAc3JhdGVxHlgN
AAAAKHVzZSBkZWZhdWx0KXEfWAsAAABzdHJlYW1fbmFtZXEgWAkAAABPdXRTdHJlYW1xIVgLAAAA
c3RyZWFtX3R5cGVxIlgHAAAAQ29udHJvbHEjWBMAAAB1c2VfZGF0YV90aW1lc3RhbXBzcSSIWBYA
AAB1c2VfbnVtcHlfb3B0aW1pemF0aW9ucSWJdS4=
</properties>
		<properties format="pickle" node_id="13">gAN9cQAoWAgAAABtZXRhZGF0YXEBfXECWA0AAABvbmx5X25vbmVtcHR5cQOIWA0AAABwcmludF9j
aGFubmVscQSJWA0AAABwcmludF9jb21wYWN0cQWIWAoAAABwcmludF9kYXRhcQaJWA0AAABwcmlu
dF9tYXJrZXJzcQeJWAsAAABwcmludF9wcm9wc3EIiVgNAAAAcHJpbnRfc3RyZWFtc3EJXXEKWAoA
AABwcmludF90aW1lcQuJWAsAAABwcmludF90cmlhbHEMiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXENY3NpcApfdW5waWNrbGVfdHlwZQpxDlgMAAAAUHlRdDUuUXRDb3JlcQ9YCgAAAFFCeXRlQXJy
YXlxEENCAdnQywADAAAAAAMLAAABRwAABHQAAAKZAAADDAAAAW0AAARzAAACmAAAAAAAAAAAB4AA
AAMMAAABbQAABHMAAAKYcRGFcRKHcRNScRRYDgAAAHNldF9icmVha3BvaW50cRWJdS4=
</properties>
		<properties format="pickle" node_id="14">gAN9cQAoWAUAAABiYW5kc3EBXXECKF1xAyhLBEsHZV1xBChLCEsMZV1xBShLDUseZV1xBihLH0sq
ZWVYCgAAAGNvbmRfZmllbGRxB1gLAAAAVGFyZ2V0VmFsdWVxCFgPAAAAaW5pdGlhbGl6ZV9vbmNl
cQmIWAgAAABtZXRhZGF0YXEKfXELWAwAAABtaW5fZmZ0X3NpemVxDE0AAlgDAAAAbm9mcQ1LAlgO
AAAAb3ZlcmxhcF9sZW5ndGhxDlgNAAAAKHVzZSBkZWZhdWx0KXEPWAwAAABvdmVybGFwX3VuaXRx
EFgHAAAAc2FtcGxlc3ERWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRJjc2lwCl91bnBpY2tsZV90
eXBlCnETWAwAAABQeVF0NS5RdENvcmVxFFgKAAAAUUJ5dGVBcnJheXEVQ0IB2dDLAAMAAAAAAwsA
AAGLAAAEdQAAAlUAAAMMAAABsQAABHQAAAJUAAAAAAAAAAAHgAAAAwwAAAGxAAAEdAAAAlRxFoVx
F4dxGFJxGVgOAAAAc2V0X2JyZWFrcG9pbnRxGolYCQAAAHNocmlua2FnZXEbSwBYCwAAAHdpbmRv
d19mdW5jcRxYBAAAAGhhbm5xHVgNAAAAd2luZG93X2xlbmd0aHEeaA9YDAAAAHdpbmRvd19wYXJh
bXEfaA9YCwAAAHdpbmRvd191bml0cSBoEXUu
</properties>
		<properties format="pickle" node_id="15">gAN9cQAoWA0AAABhYnNvbHV0ZV90aW1lcQGJWA0AAABhbHdheXNfb25fdG9wcQKJWAsAAABhbnRp
YWxpYXNlZHEDiFgQAAAAYXV0b19saW5lX2NvbG9yc3EEiVgJAAAAYXV0b3NjYWxlcQWIWBAAAABi
YWNrZ3JvdW5kX2NvbG9ycQZYBwAAACNGRkZGRkZxB1gQAAAAZGVjb3JhdGlvbl9jb2xvcnEIWAcA
AAAjMDAwMDAwcQlYCwAAAGRvd25zYW1wbGVkcQqJWAkAAABmb250X3NpemVxC0dAJAAAAAAAAFgM
AAAAaW5pdGlhbF9kaW1zcQxdcQ0oSzJLMk28Ak30AWVYCgAAAGxpbmVfY29sb3JxDlgHAAAAIzAw
MDAwMHEPWAoAAABsaW5lX3dpZHRocRBHP+gAAAAAAABYDAAAAG1hcmtlcl9jb2xvcnERWAcAAAAj
RkYwMDAwcRJYCAAAAG1ldGFkYXRhcRN9cRRYDAAAAG5hbnNfYXNfemVyb3EViVgOAAAAbm9fY29u
Y2F0ZW5hdGVxFolYDgAAAG92ZXJyaWRlX3NyYXRlcRdYDQAAACh1c2UgZGVmYXVsdClxGFgMAAAA
cGxvdF9tYXJrZXJzcRmIWAsAAABwbG90X21pbm1heHEaiFgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEbY3NpcApfdW5waWNrbGVfdHlwZQpxHFgMAAAAUHlRdDUuUXRDb3JlcR1YCgAAAFFCeXRlQXJy
YXlxHkNCAdnQywADAAAAAAMMAAABJwAABHMAAALeAAADDAAAAScAAARzAAAC3gAAAAAAAAAAB4AA
AAMMAAABJwAABHMAAALecR+FcSCHcSFScSJYBQAAAHNjYWxlcSNHP/AAAAAAAABYDgAAAHNldF9i
cmVha3BvaW50cSSJWAwAAABzaG93X3Rvb2xiYXJxJYlYCwAAAHN0cmVhbV9uYW1lcSZoGFgKAAAA
dGltZV9yYW5nZXEnR0AUAAAAAAAAWAUAAAB0aXRsZXEoWBAAAABUaW1lIHNlcmllcyB2aWV3cSlY
CgAAAHplcm9fY29sb3JxKlgHAAAAIzdGN0Y3RnErWAgAAAB6ZXJvbWVhbnEsiHUu
</properties>
		<properties format="pickle" node_id="16">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWB8AAABhcHBseV90aW1lX3NlbGVjdGlv
bl90b19tYXJrZXJzcQKJWAQAAABheGlzcQNYBwAAAGZlYXR1cmVxBFgIAAAAbWV0YWRhdGFxBX1x
BlgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEHY3NpcApfdW5waWNrbGVfdHlwZQpxCFgMAAAAUHlR
dDUuUXRDb3JlcQlYCgAAAFFCeXRlQXJyYXlxCkNCAdnQywADAAAAAAMMAAABpwAABHMAAAJeAAAD
DAAAAacAAARzAAACXgAAAAAAAAAAB4AAAAMMAAABpwAABHMAAAJecQuFcQyHcQ1ScQ5YCQAAAHNl
bGVjdGlvbnEPXXEQSwBhWA4AAABzZXRfYnJlYWtwb2ludHERiVgEAAAAdW5pdHESWAcAAABpbmRp
Y2VzcRN1Lg==
</properties>
		<properties format="pickle" node_id="17">gAN9cQAoWA0AAABhbHdheXNfb25fdG9wcQGJWA8AAABhdXRvX2Jhcl9jb2xvcnNxAolYBAAAAGF4
aXNxA1gHAAAAZmVhdHVyZXEEWBAAAABiYWNrZ3JvdW5kX2NvbG9ycQVYBwAAACNGRkZGRkZxBlgJ
AAAAYmFyX2NvbG9ycQdYAQAAAGJxCFgJAAAAYmFyX3dpZHRocQlHP+zMzMzMzM1YCQAAAGZvbnRf
c2l6ZXEKR0AkAAAAAAAAWAwAAABpbml0aWFsX2RpbXNxC11xDChNIANLMk28Ak30AWVYDgAAAGlu
c3RhbmNlX2ZpZWxkcQ1YDQAAACh1c2UgZGVmYXVsdClxDlgOAAAAbGFiZWxfcm90YXRpb25xD1gK
AAAAaG9yaXpvbnRhbHEQWAgAAABtZXRhZGF0YXERfXESWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5
cRNjc2lwCl91bnBpY2tsZV90eXBlCnEUWAwAAABQeVF0NS5RdENvcmVxFVgKAAAAUUJ5dGVBcnJh
eXEWQ0IB2dDLAAMAAAAAAwsAAAEjAAAEdAAAAr0AAAMMAAABSQAABHMAAAK8AAAAAAAAAAAHgAAA
AwwAAAFJAAAEcwAAArxxF4VxGIdxGVJxGlgOAAAAc2V0X2JyZWFrcG9pbnRxG4lYDAAAAHNob3df
dG9vbGJhcnEciVgLAAAAc3RyZWFtX25hbWVxHVgNAAAAKHVzZSBkZWZhdWx0KXEeWAUAAAB0aXRs
ZXEfWA4AAABDbGFzc2lmaWNhdGlvbnEgWBEAAAB1c2VfbGFzdF9pbnN0YW5jZXEhiFgHAAAAdmVy
Ym9zZXEiiVgIAAAAeV9saW1pdHNxI11xJChLAEsBZXUu
</properties>
		<properties format="pickle" node_id="18">gAN9cQAoWA8AAABheGlzX29jY3VycmVuY2VxAUsAWBAAAABjYXJyeV9vdmVyX25hbWVzcQKIWBIA
AABjYXJyeV9vdmVyX251bWJlcnNxA4lYDAAAAGN1c3RvbV9sYWJlbHEEWA0AAAAodXNlIGRlZmF1
bHQpcQVYCAAAAGRlY2ltYWxzcQZLA1gJAAAAaW5pdF9kYXRhcQddcQgoWAQAAABzbmFwcQlYBwAA
AG5vdGhpbmdxCmVYCwAAAGpvaW5fZm9ybWF0cQtYBQAAAHtuZXd9cQxYEQAAAGtlZXBfb3RoZXJf
YXJyYXlzcQ2JWAoAAABrZWVwX3Byb3BzcQ6JWAgAAABtZXRhZGF0YXEPfXEQWAgAAABuZXdfYXhp
c3ERWAcAAABmZWF0dXJlcRJYCAAAAG9sZF9heGlzcRNYBwAAAGZlYXR1cmVxFFgMAAAAb25seV9z
aWduYWxzcRWJWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRZjc2lwCl91bnBpY2tsZV90eXBlCnEX
WAwAAABQeVF0NS5RdENvcmVxGFgKAAAAUUJ5dGVBcnJheXEZQ0IB2dDLAAMAAP/////////3AAAH
gAAABAYAAAMMAAABfwAABHMAAAKGAAAAAAIAAAAHgAAAAAAAAAAdAAAHfwAABAVxGoVxG4dxHFJx
HVgOAAAAc2V0X2JyZWFrcG9pbnRxHolYCQAAAHZlcmJvc2l0eXEfSwB1Lg==
</properties>
		<properties format="pickle" node_id="19">gAN9cQAoWAQAAABheGlzcQFYCAAAAGluc3RhbmNlcQJYEgAAAGZvcmNlX2ZlYXR1cmVfYXhpc3ED
iVgLAAAAaWdub3JlX25hbnNxBIlYCAAAAG1ldGFkYXRhcQV9cQZYBgAAAHJvYnVzdHEHiVgVAAAA
cm9idXN0X2VzdGltYXRvcl90eXBlcQhYBgAAAG1lZGlhbnEJWBMAAABzYXZlZFdpZGdldEdlb21l
dHJ5cQpjc2lwCl91bnBpY2tsZV90eXBlCnELWAwAAABQeVF0NS5RdENvcmVxDFgKAAAAUUJ5dGVB
cnJheXENQ0IB2dDLAAMAAAAAAwsAAAF1AAAEdAAAAmsAAAMMAAABmwAABHMAAAJqAAAAAAAAAAAH
gAAAAwwAAAGbAAAEcwAAAmpxDoVxD4dxEFJxEVgOAAAAc2V0X2JyZWFrcG9pbnRxEolYDwAAAHRy
aW1fcHJvcG9ydGlvbnETRz+5mZmZmZmadS4=
</properties>
		<properties format="pickle" node_id="20">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWFYAAABDOi9Vc2Vycy9hY2hha3JhYm9ydHkvT25lRHJpdmUgLSBPbGluIENv
bGxlZ2Ugb2YgRW5naW5lZXJpbmcvRG9jdW1lbnRzL0hBTC9qaWF5dWFuLnhkZnEIWBMAAABoYW5k
bGVfY2xvY2tfcmVzZXRzcQmIWBEAAABoYW5kbGVfY2xvY2tfc3luY3EKiFgVAAAAaGFuZGxlX2pp
dHRlcl9yZW1vdmFscQuIWA4AAABtYXhfbWFya2VyX2xlbnEMWA0AAAAodXNlIGRlZmF1bHQpcQ1Y
CAAAAG1ldGFkYXRhcQ59cQ9YEgAAAHJlb3JkZXJfdGltZXN0YW1wc3EQiVgOAAAAcmV0YWluX3N0
cmVhbXNxEWgNWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRJjc2lwCl91bnBpY2tsZV90eXBlCnET
WAwAAABQeVF0NS5RdENvcmVxFFgKAAAAUUJ5dGVBcnJheXEVQ0IB2dDLAAMAAAAAAwsAAAFiAAAE
dAAAAn4AAAMMAAABiAAABHMAAAJ9AAAAAAAAAAAHgAAAAwwAAAGIAAAEcwAAAn1xFoVxF4dxGFJx
GVgOAAAAc2V0X2JyZWFrcG9pbnRxGolYCwAAAHVzZV9jYWNoaW5ncRuJWA8AAAB1c2Vfc3RyZWFt
bmFtZXNxHIlYBwAAAHZlcmJvc2VxHYl1Lg==
</properties>
		<properties format="pickle" node_id="21">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWFYAAABDOi9Vc2Vycy9hY2hha3JhYm9ydHkvT25lRHJpdmUgLSBPbGluIENv
bGxlZ2Ugb2YgRW5naW5lZXJpbmcvRG9jdW1lbnRzL0hBTC9qaWF5dWFuLnhkZnEIWBMAAABoYW5k
bGVfY2xvY2tfcmVzZXRzcQmIWBEAAABoYW5kbGVfY2xvY2tfc3luY3EKiFgVAAAAaGFuZGxlX2pp
dHRlcl9yZW1vdmFscQuIWA4AAABtYXhfbWFya2VyX2xlbnEMWA0AAAAodXNlIGRlZmF1bHQpcQ1Y
CAAAAG1ldGFkYXRhcQ59cQ9YEgAAAHJlb3JkZXJfdGltZXN0YW1wc3EQiVgOAAAAcmV0YWluX3N0
cmVhbXNxEWgNWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRJjc2lwCl91bnBpY2tsZV90eXBlCnET
WAwAAABQeVF0NS5RdENvcmVxFFgKAAAAUUJ5dGVBcnJheXEVQ0IB2dDLAAMAAAAAAwsAAAFiAAAE
dAAAAn4AAAMMAAABiAAABHMAAAJ9AAAAAAAAAAAHgAAAAwwAAAGIAAAEcwAAAn1xFoVxF4dxGFJx
GVgOAAAAc2V0X2JyZWFrcG9pbnRxGolYCwAAAHVzZV9jYWNoaW5ncRuJWA8AAAB1c2Vfc3RyZWFt
bmFtZXNxHIlYBwAAAHZlcmJvc2VxHYl1Lg==
</properties>
		<properties format="literal" node_id="22">{'entire_packet': True, 'metadata': {}, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'threshold': 10}</properties>
		<properties format="pickle" node_id="23">gAN9cQAoWA0AAABhbHdheXNfb25fdG9wcQGIWAoAAABhdXRvX2Nsb3NlcQKIWAgAAABjb2xfYXhp
c3EDWAQAAAB0aW1lcQRYCAAAAGRlY2ltYWxzcQVLBlgNAAAAZXZlcnlfbl90aWNrc3EGSwFYDQAA
AGZld2VyX2J1dHRvbnNxB4lYCQAAAGZvbnRfc2l6ZXEISwpYEAAAAGluaXRpYWxfcG9zaXRpb25x
CV1xCihLFEsyTfQBTZABZVgIAAAAbWV0YWRhdGFxC31xDFgIAAAAcm93X2F4aXNxDVgFAAAAc3Bh
Y2VxDlgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEPY3NpcApfdW5waWNrbGVfdHlwZQpxEFgMAAAA
UHlRdDUuUXRDb3JlcRFYCgAAAFFCeXRlQXJyYXlxEkNCAdnQywADAAAAAAMLAAABJwAABHQAAAK5
AAADDAAAAU0AAARzAAACuAAAAAAAAAAAB4AAAAMMAAABTQAABHMAAAK4cROFcRSHcRVScRZYDgAA
AHNldF9icmVha3BvaW50cReJWA8AAABzaG93X2F4ZXNfdGFibGVxGIhYDwAAAHNob3dfZGF0YV90
YWJsZXEZiFgSAAAAc2hvd19tYXJrZXJzX3RhYmxlcRqIWBAAAABzaG93X21heF9jb2x1bW5zcRtL
FFgPAAAAc2hvd19tYXhfdmFsdWVzcRxLMlgSAAAAc2hvd19zdHJlYW1zX3RhYmxlcR2IWAsAAABz
dHJlYW1fbmFtZXEeWA0AAAAodXNlIGRlZmF1bHQpcR9YDAAAAHdpbmRvd190aXRsZXEgWBMAAABJ
bnNwZWN0IERhdGEgUGFja2V0cSF1Lg==
</properties>
	</node_properties>
	<patch>{
    "description": {
        "description": "(description missing)",
        "license": "",
        "name": "(untitled)",
        "status": "(unspecified)",
        "url": "",
        "version": "0.0.0"
    },
    "edges": [
        [
            "node3",
            "data",
            "node6",
            "data"
        ],
        [
            "node6",
            "data",
            "node4",
            "data"
        ],
        [
            "node5",
            "data",
            "node8",
            "data"
        ],
        [
            "node8",
            "data",
            "node1",
            "data"
        ],
        [
            "node7",
            "data",
            "node9",
            "streaming_data"
        ],
        [
            "node7",
            "data",
            "node24",
            "data"
        ],
        [
            "node9",
            "data",
            "node5",
            "data"
        ],
        [
            "node10",
            "data",
            "node11",
            "data"
        ],
        [
            "node12",
            "data",
            "node7",
            "data"
        ],
        [
            "node4",
            "data",
            "node14",
            "data"
        ],
        [
            "node4",
            "data",
            "node19",
            "data"
        ],
        [
            "node4",
            "data",
            "node23",
            "data"
        ],
        [
            "node15",
            "data",
            "node3",
            "data"
        ],
        [
            "node21",
            "data",
            "node9",
            "calib_data"
        ],
        [
            "node22",
            "data",
            "node10",
            "data"
        ],
        [
            "node23",
            "data",
            "node17",
            "data"
        ],
        [
            "node17",
            "data",
            "node16",
            "data"
        ],
        [
            "node17",
            "data",
            "node13",
            "data"
        ],
        [
            "node19",
            "data",
            "node20",
            "data"
        ],
        [
            "node20",
            "data",
            "node18",
            "data"
        ],
        [
            "node1",
            "data",
            "node2",
            "data"
        ],
        [
            "node2",
            "data",
            "node15",
            "data"
        ]
    ],
    "nodes": {
        "node1": {
            "class": "FIRFilter",
            "module": "neuropype.nodes.signal_processing.FIRFilter",
            "params": {
                "antisymmetric": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "convolution_method": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "standard"
                },
                "cut_preringing": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        2.0,
                        4.0,
                        42.0,
                        45.0
                    ]
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "minimum_phase": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "mode": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "bandpass"
                },
                "order": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stop_atten": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 50.0
                }
            },
            "uuid": "98d79c91-0996-4ee1-a2b4-7c3375aeece9"
        },
        "node10": {
            "class": "StreamData",
            "module": "neuropype.nodes.formatting.StreamData",
            "params": {
                "data_dtype": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "float64"
                },
                "hitch_probability": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "jitter_percent": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5
                },
                "log_progress": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "looping": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "randseed": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 34535
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "speedup": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "start_pos": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "timestamp_jitter": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "timing": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "wallclock"
                },
                "update_interval": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.04
                }
            },
            "uuid": "7d36ab62-7cb5-4b48-bdae-a28896efa7ad"
        },
        "node11": {
            "class": "LSLOutput",
            "module": "neuropype.nodes.network.LSLOutput",
            "params": {
                "chunk_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "ignore_signal_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "keep_singleton_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Marker"
                },
                "marker_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "MyMarkerStream"
                },
                "marker_source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_buffered": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 60
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "numeric_label_precision": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                },
                "numeric_marker_precision": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 3
                },
                "reset_if_labels_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "send_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "separator": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "-"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "source_id": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "mysourceid234"
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "OutStreamData"
                },
                "stream_type": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "EEG"
                },
                "use_data_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_numpy_optimization": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "b38757d3-d8c7-4173-a1ec-2d272494b5d4"
        },
        "node12": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "data_dtype": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "float64"
                },
                "diagnostics": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "exclude_desc_fields": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "marker_query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "name='MyMarkerStream'"
                },
                "max_blocklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1024
                },
                "max_buflen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "max_chunklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "nominal_rate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "omit_desc": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "prealloc_buffer": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "proc_clocksync": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "proc_dejitter": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "proc_monotonize": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "proc_threadsafe": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "name='obci_eeg1'"
                },
                "recover": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "resolve_minimum_time": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "f7512141-2966-4108-93c3-2ed872c38346"
        },
        "node13": {
            "class": "LSLOutput",
            "module": "neuropype.nodes.network.LSLOutput",
            "params": {
                "chunk_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "ignore_signal_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "keep_singleton_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Marker"
                },
                "marker_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "OutStream-markers"
                },
                "marker_source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_buffered": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 60
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "numeric_label_precision": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                },
                "numeric_marker_precision": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 3
                },
                "reset_if_labels_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "send_markers": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "separator": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "-"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "source_id": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "(never use same source id in one pypeline)"
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "OutStream"
                },
                "stream_type": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Control"
                },
                "use_data_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_numpy_optimization": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "463d4338-87cc-44d1-a544-b46552d63c98"
        },
        "node14": {
            "class": "PrintToConsole",
            "module": "neuropype.nodes.diagnostics.PrintToConsole",
            "params": {
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "only_nonempty": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "print_channel": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_compact": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "print_data": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_props": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_streams": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "print_time": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_trial": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "468177f4-911b-42ab-87ba-aa1b0553298d"
        },
        "node15": {
            "class": "FilterBankCommonSpatialPattern",
            "module": "neuropype.nodes.neural.FilterBankCommonSpatialPattern",
            "params": {
                "bands": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        [
                            4,
                            7
                        ],
                        [
                            8,
                            12
                        ],
                        [
                            13,
                            30
                        ],
                        [
                            31,
                            42
                        ]
                    ]
                },
                "cond_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "TargetValue"
                },
                "initialize_once": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "min_fft_size": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 512
                },
                "nof": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 2
                },
                "overlap_length": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "overlap_unit": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "samples"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "shrinkage": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0
                },
                "window_func": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "hann"
                },
                "window_length": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "window_param": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "window_unit": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "samples"
                }
            },
            "uuid": "ead8a35c-bafb-4d87-ad39-bcd9b51088be"
        },
        "node16": {
            "class": "TimeSeriesPlot",
            "module": "neuropype.nodes.visualization.TimeSeriesPlot",
            "params": {
                "absolute_time": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "antialiased": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "auto_line_colors": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "autoscale": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "decoration_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "downsampled": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "font_size": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 10.0
                },
                "initial_dims": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        50,
                        50,
                        700,
                        500
                    ]
                },
                "line_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "line_width": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.75
                },
                "marker_color": {
                    "customized": false,
                    "type": "Port",
                    "value": "#FF0000"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "nans_as_zero": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "no_concatenate": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "override_srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "plot_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "plot_minmax": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "scale": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "time_range": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5.0
                },
                "title": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Time series view"
                },
                "zero_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#7F7F7F"
                },
                "zeromean": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                }
            },
            "uuid": "c84d73ee-5951-471e-ae82-a2893a41b9bc"
        },
        "node17": {
            "class": "SelectRange",
            "module": "neuropype.nodes.tensor_math.SelectRange",
            "params": {
                "apply_multiple_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "apply_time_selection_to_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "selection": {
                    "customized": true,
                    "type": "Port",
                    "value": [
                        0
                    ]
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "unit": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "indices"
                }
            },
            "uuid": "0e63393b-5e5d-4219-8537-144c8bbb39f0"
        },
        "node18": {
            "class": "BarPlot",
            "module": "neuropype.nodes.visualization.BarPlot",
            "params": {
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "auto_bar_colors": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "bar_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "b"
                },
                "bar_width": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 0.9
                },
                "font_size": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 10.0
                },
                "initial_dims": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        800,
                        50,
                        700,
                        500
                    ]
                },
                "instance_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "label_rotation": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "horizontal"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "title": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "Classification"
                },
                "use_last_instance": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "y_limits": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        0,
                        1
                    ]
                }
            },
            "uuid": "1d6def26-8b14-4401-b8cb-883bdf3e1304"
        },
        "node19": {
            "class": "OverrideAxis",
            "module": "neuropype.nodes.tensor_math.OverrideAxis",
            "params": {
                "axis_occurrence": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "carry_over_names": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "carry_over_numbers": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "custom_label": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "decimals": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 3
                },
                "init_data": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "snap",
                        "nothing"
                    ]
                },
                "join_format": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "{new}"
                },
                "keep_other_arrays": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "keep_props": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "new_axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "old_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "only_signals": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbosity": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                }
            },
            "uuid": "77a72ff6-8465-4368-a4b3-81afccfcd480"
        },
        "node2": {
            "class": "Segmentation",
            "module": "neuropype.nodes.formatting.Segmentation",
            "params": {
                "keep_marker_chunk": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "max_gap_length": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.2
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "online_epoching": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "marker-locked"
                },
                "sample_offset": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "select_markers": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "time_bounds": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        0,
                        2
                    ]
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "f8a86dac-f39f-43b1-804a-099c9372700e"
        },
        "node20": {
            "class": "Mean",
            "module": "neuropype.nodes.statistics.Mean",
            "params": {
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "instance"
                },
                "force_feature_axis": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "ignore_nans": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "robust": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "robust_estimator_type": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "median"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "trim_proportion": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.1
                }
            },
            "uuid": "fe04ef1a-5678-4ff9-ac4d-e7b9bcf0e495"
        },
        "node21": {
            "class": "ImportXDF",
            "module": "neuropype.nodes.file_system.ImportXDF",
            "params": {
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/achakraborty/OneDrive - Olin College of Engineering/Documents/HAL/jiayuan.xdf"
                },
                "handle_clock_resets": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "handle_clock_sync": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "handle_jitter_removal": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "max_marker_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "reorder_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retain_streams": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_caching": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_streamnames": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "0e547a28-1407-4a86-b037-1148fe23dc4c"
        },
        "node22": {
            "class": "ImportXDF",
            "module": "neuropype.nodes.file_system.ImportXDF",
            "params": {
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/achakraborty/OneDrive - Olin College of Engineering/Documents/HAL/jiayuan.xdf"
                },
                "handle_clock_resets": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "handle_clock_sync": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "handle_jitter_removal": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "max_marker_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "reorder_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retain_streams": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_caching": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_streamnames": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "d8dfcc97-a3dd-4a25-bfb9-10392885c091"
        },
        "node23": {
            "class": "DiscardLongChunks",
            "module": "neuropype.nodes.utilities.DiscardLongChunks",
            "params": {
                "entire_packet": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "threshold": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 10
                }
            },
            "uuid": "b7f4ade1-28a9-408a-aa2d-5766c78abc6d"
        },
        "node24": {
            "class": "InspectData",
            "module": "neuropype.nodes.visualization.InspectData",
            "params": {
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "auto_close": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "col_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "decimals": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 6
                },
                "every_n_ticks": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                },
                "fewer_buttons": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "font_size": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 10
                },
                "initial_position": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        20,
                        50,
                        500,
                        400
                    ]
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "row_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "space"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_axes_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "show_data_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "show_markers_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "show_max_columns": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 20
                },
                "show_max_values": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 50
                },
                "show_streams_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "window_title": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Inspect Data Packet"
                }
            },
            "uuid": "3bc5a10d-7b1a-4190-813e-fdcb0720b649"
        },
        "node3": {
            "class": "Variance",
            "module": "neuropype.nodes.statistics.Variance",
            "params": {
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "time"
                },
                "degrees_of_freedom": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "force_feature_axis": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "1be6244d-2f49-4f3e-a734-43458675f577"
        },
        "node4": {
            "class": "LogisticRegression",
            "module": "neuropype.nodes.machine_learning.LogisticRegression",
            "params": {
                "alphas": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        0.1,
                        0.5,
                        1.0,
                        5,
                        10.0
                    ]
                },
                "bias_scaling": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "class_weights": {
                    "customized": true,
                    "type": "Port",
                    "value": "auto"
                },
                "cond_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "TargetValue"
                },
                "dont_reset_model": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "dual_formulation": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "feature_scaling": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "none"
                },
                "include_bias": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "initialize_once": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "l1_ratios": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "max_iter": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 100
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "multiclass": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "ovr"
                },
                "num_folds": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 5
                },
                "num_jobs": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                },
                "probabilistic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "random_seed": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 12345
                },
                "regularizer": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "l2"
                },
                "search_metric": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "accuracy"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "solver": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "lbfgs"
                },
                "tolerance": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0001
                },
                "verbosity": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                }
            },
            "uuid": "7e764997-fbb3-4ca1-bbcd-8bf4f291697b"
        },
        "node5": {
            "class": "AssignTargets",
            "module": "neuropype.nodes.machine_learning.AssignTargets",
            "params": {
                "also_legacy_output": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "is_categorical": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "iv_column": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Marker"
                },
                "mapping": {
                    "customized": true,
                    "type": "Port",
                    "value": {
                        "0s": 0,
                        "3s": 1
                    }
                },
                "mapping_format": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "compat"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "support_wildcards": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_numbers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "59c9d795-9879-4b5e-822d-d21df1a7ec84"
        },
        "node6": {
            "class": "Logarithm",
            "module": "neuropype.nodes.elementwise_math.Logarithm",
            "params": {
                "base": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "56bb438d-1550-40bb-a2b6-eb22b4601632"
        },
        "node7": {
            "class": "DejitterTimestamps",
            "module": "neuropype.nodes.utilities.DejitterTimestamps",
            "params": {
                "force_monotonic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "forget_halftime": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 300
                },
                "max_updaterate": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 500
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "warmup_samples": {
                    "customized": false,
                    "type": "IntPort",
                    "value": -1
                }
            },
            "uuid": "c61aafae-4777-4b41-8104-3eae4ba01ac2"
        },
        "node8": {
            "class": "SelectRange",
            "module": "neuropype.nodes.tensor_math.SelectRange",
            "params": {
                "apply_multiple_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "apply_time_selection_to_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "space"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "selection": {
                    "customized": true,
                    "type": "Port",
                    "value": ":-6"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "unit": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "indices"
                }
            },
            "uuid": "a3c0fbb3-d252-4693-a392-bbe91816ad15"
        },
        "node9": {
            "class": "InjectCalibrationData",
            "module": "neuropype.nodes.machine_learning.InjectCalibrationData",
            "params": {
                "delay_streaming_packets": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "a9e56eff-173f-4703-b66f-6e72b51ce559"
        }
    },
    "version": 1.1
}</patch>
</scheme>
