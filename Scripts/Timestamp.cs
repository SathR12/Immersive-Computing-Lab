using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;

public class Timestamp : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        File.WriteAllText(@"C:\Users\ARISE_students\VR_data\time_data.txt", "### Purged Previous Times ###\n");

    }

    // Update is called once per frame
    void Update()
    {
        string timestamp = DateTime.Now.ToString("HH:mm:ss");
        File.AppendAllText(@"C:\Users\ARISE_students\VR_data\time_data.txt", timestamp + "\n"); 
        //Debug.Log(timestamp);
    }
}
