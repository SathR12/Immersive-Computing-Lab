using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
using TMPro;

public class TextMeshModifier : MonoBehaviour
{
    private string path = @"C:\Users\ARISE_students\VR_data\sample_text.txt";
    public TMP_Text canvasText;
    //public TMP_Text gameObjectText;
    // Start is called before the first frame update
    void Start()
    {
        Debug.Log("Script has started");

        canvasText.text = File.ReadAllText(path);
        //gameObjectText.text = "welcome to unity";
    }

    // Update is called once per frame
    void Update()
    {

    }
}
