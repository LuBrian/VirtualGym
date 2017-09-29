package com.example.panchy.virtualgym.ModelClass;

import java.util.ArrayList;
import java.util.Date;

/**
 * Created by Panchy on 2017/9/28.
 */

public class Comment {
    private String commentDescription;
    private  int posterID;
    private Date dataTime;
    private ArrayList<Reply> replyList;

    public Comment(String commentDescription, int posterID, Date dataTime,
                   ArrayList<Reply> replyList) {
        this.commentDescription = commentDescription;
        this.posterID = posterID;
        this.dataTime = dataTime;
        this.replyList = replyList;
    }

    public String getCommentDescription() {
        return commentDescription;
    }

    public void setCommentDescription(String commentDescription) {
        this.commentDescription = commentDescription;
    }

    public int getPosterID() {
        return posterID;
    }

    public void setPosterID(int posterID) {
        this.posterID = posterID;
    }

    public Date getDataTime() {
        return dataTime;
    }

    public void setDataTime(Date dataTime) {
        this.dataTime = dataTime;
    }

    public ArrayList<Reply> getReplyList() {
        return replyList;
    }

    public void setReplyList(ArrayList<Reply> replyList) {
        this.replyList = replyList;
    }
}
