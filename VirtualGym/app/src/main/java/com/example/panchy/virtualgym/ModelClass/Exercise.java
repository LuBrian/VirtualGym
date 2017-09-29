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

    public Exercise(String exerciseDescription, String exerciseTag, int exerciseID,
                    int exercisePosterID, Image exercisePicture, Date exerciseDate,
                    String[] referenceList, ArrayList<Comment> commentLost) {
        this.exerciseDescription = exerciseDescription;
        this.exerciseTag = exerciseTag;
        this.exerciseID = exerciseID;
        this.exercisePosterID = exercisePosterID;
        this.exercisePicture = exercisePicture;
        this.exerciseDate = exerciseDate;
        this.referenceList = referenceList;
        this.commentLost = commentLost;
    }

    public String getExerciseDescription() {
        return exerciseDescription;
    }

    public void setExerciseDescription(String exerciseDescription) {
        this.exerciseDescription = exerciseDescription;
    }

    public String getExerciseTag() {
        return exerciseTag;
    }

    public void setExerciseTag(String exerciseTag) {
        this.exerciseTag = exerciseTag;
    }

    public int getExerciseID() {
        return exerciseID;
    }

    public void setExerciseID(int exerciseID) {
        this.exerciseID = exerciseID;
    }

    public int getExercisePosterID() {
        return exercisePosterID;
    }

    public void setExercisePosterID(int exercisePosterID) {
        this.exercisePosterID = exercisePosterID;
    }

    public Image getExercisePicture() {
        return exercisePicture;
    }

    public void setExercisePicture(Image exercisePicture) {
        this.exercisePicture = exercisePicture;
    }

    public Date getExerciseDate() {
        return exerciseDate;
    }

    public void setExerciseDate(Date exerciseDate) {
        this.exerciseDate = exerciseDate;
    }

    public String[] getReferenceList() {
        return referenceList;
    }

    public void setReferenceList(String[] referenceList) {
        this.referenceList = referenceList;
    }

    public ArrayList<Comment> getCommentLost() {
        return commentLost;
    }

    public void setCommentLost(ArrayList<Comment> commentLost) {
        this.commentLost = commentLost;
    }
}
