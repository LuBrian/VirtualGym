package com.example.panchy.virtualgym.ModelClass;

import android.media.Image;

import java.util.ArrayList;
import java.util.Date;

/**
 * Created by Panchy on 2017/9/28.
 */

public class Exercise {
    private String exerciseDescription;
    private String exerciseTag;
    private int exerciseID;
    private int exercisePosterID;
    private Image exercisePicture;
    //private Json exerciseData;
    private Date exerciseDate;
    private String[] referenceList;
    private ArrayList<Comment> commentLost;
}
