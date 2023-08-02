using UnityEngine;
using UnityEngine.XR;
using System.IO;

public class HeadTracker : MonoBehaviour
{
    private Vector3 headPosition;
    private InputDevice device;
    private Quaternion headRotation;

    void Start()
    {
        //clears the eye data from the previous run 
        File.WriteAllText(@"C:\Users\ARISE_students\VR_data\head_data.txt", "### Purged Previous Head Data ###\n");
        
    }

    void Update()
    {
        device = InputDevices.GetDeviceAtXRNode(XRNode.Head);

        if (device.TryGetFeatureValue(CommonUsages.devicePosition, out headPosition)) //keyword out is passing by reference and putting data into that variable
        {
            Debug.Log("Head Position: " + headPosition);
        }

        else
        {
            Debug.Log("Device is not supported or not active");
        }

        if (device.TryGetFeatureValue(CommonUsages.deviceRotation, out headRotation)) //use CommonUsages for any device node that involves rotation or position attributes 
        {
            Debug.Log("Head Rotation: " + headRotation.eulerAngles);
        }

        else
        {
            Debug.Log("Device is not supported or not active");
        }


        /*
        File.AppendAllText(
            @"C:\Users\ARISE_students\VR_data\head_data.txt",
            "\nHead Position: " + headPosition +
            "\nHead Rotation: " + headRotation
            );

        */

       
        File.AppendAllText(
            @"C:\Users\ARISE_students\VR_data\head_data.txt",
            headPosition + "\n" + 
            headRotation + "\n"
            );

        

    }
       
}