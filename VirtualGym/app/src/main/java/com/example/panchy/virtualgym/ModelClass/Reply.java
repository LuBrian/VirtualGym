package com.example.panchy.virtualgym.ModelClass;

import java.sql.Date;

/**
 * Created by Panchy on 2017/9/28.
 */

public class Reply {
    private String replyDescription;
    private int posterID;
    private Date dateTime;

    public Reply(String replyDescription, int posterID, Date dateTime) {
        this.replyDescription = replyDescription;
        this.posterID = posterID;
        this.dateTime = dateTime;
    }

    public String getReplyDescription() {
        return replyDescription;
    }

    public void setReplyDescription(String replyDescription) {
        this.replyDescription = replyDescription;
    }

    public int getPosterID() {
        return posterID;
    }

    public void setPosterID(int posterID) {
        this.posterID = posterID;
    }

    public Date getDateTime() {
        return dateTime;
    }

    public void setDateTime(Date dateTime) {
        this.dateTime = dateTime;
    }


}
