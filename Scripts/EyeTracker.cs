using UnityEngine;
using UnityEngine.XR;
using System.IO;

public class EyeTracker : MonoBehaviour
{
 
    void Start()
    {
        //clears the eye data from the previous run 
        //File.WriteAllText(@"C:\Users\ARISE_students\VR_data\eye_data.txt", "### Purged Previous Eye Data ###\n");
        File.WriteAllText(@"C:\Users\ARISE_students\VR_data\left_eye_data.txt", "### Purged Previous Eye Data ###\n");
        File.WriteAllText(@"C:\Users\ARISE_students\VR_data\right_eye_data.txt", "### Purged Previous Eye Data ###\n");
    }
    void Update()
    {
        InputDevice device = InputDevices.GetDeviceAtXRNode(XRNode.Head);
        Vector3 leftEyePosition, rightEyePosition;
        if (device.TryGetFeatureValue(CommonUsages.leftEyePosition, out leftEyePosition))
        {
            Debug.Log("Left Eye Position: " + leftEyePosition);
            //File.AppendAllText(@"C:\Users\ARISE_students\VR_data\eye_data.txt", "Left Eye Pos: " + leftEyePosition);
        }

        else
        {
            Debug.Log("Device is not supported or not active");
        }

        if (device.TryGetFeatureValue(CommonUsages.rightEyePosition, out rightEyePosition))
        {
            Debug.Log("Right Eye Position: " + rightEyePosition);
            //File.WriteAllText(@"C:\Users\ARISE_students\VR_data\eye_data.txt", "Right Eye Pos: " + rightEyePosition);
        }

        else
        {
            Debug.Log("Device is not supported or not active");
        }

        Quaternion leftEyeRotation, rightEyeRotation;
        if (device.TryGetFeatureValue(CommonUsages.leftEyeRotation, out leftEyeRotation))
        {
            Debug.Log("Left Eye Rotation: " + leftEyeRotation.eulerAngles);
        }

        else
        {
            Debug.Log("Device is not supported or not active");
        }

        if (device.TryGetFeatureValue(CommonUsages.rightEyeRotation, out rightEyeRotation))
        {
            Debug.Log("Right Eye Rotation: " + rightEyeRotation.eulerAngles);
        }

        else
        {
            Debug.Log("Device is not supported or not active");
        }

        
         File.AppendAllText(
            @"C:\Users\ARISE_students\VR_data\eye_data.txt", 
            "\nLeft Eye Position: " + leftEyePosition + 
            "\nRight Eye Position: " + rightEyePosition + 
            "\nLeft Eye Rotation: " + leftEyeRotation.eulerAngles + 
            "\nRight Eye Rotation: " + rightEyeRotation.eulerAngles
            );
        

        
        File.AppendAllText(
            @"C:\Users\ARISE_students\VR_data\left_eye_data.txt",
            leftEyePosition + "\n" +
            leftEyeRotation.eulerAngles + "\n"
            );

        File.AppendAllText(
            @"C:\Users\ARISE_students\VR_data\right_eye_data.txt",
            rightEyePosition + "\n" +
            rightEyeRotation.eulerAngles + "\n"
            );

    }
}