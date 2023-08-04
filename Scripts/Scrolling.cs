using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;


public class Scrolling : MonoBehaviour
{
    public Scrollbar scrollbar;
    // Start is called before the first frame update
    void Start()
    {
        scrollbar = GameObject.Find("Scrollbar Vertical").GetComponent<Scrollbar>();
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKey(KeyCode.UpArrow))
        {
            scrollbar.value += 0.0001f;
        }
        else if (Input.GetKey(KeyCode.DownArrow))
        {
            scrollbar.value -= 0.0001f;
        }
    }
}
