package com.example.panchy.virtualgym.ModelClass;

import android.media.Image;

/**
 * Created by Panchy on 2017/9/28.
 */

public class User {
    private String userName;
    private String userType;
    private int userID;
    private Image userPicture;
    private int[] favoriteExeList;

    public User(String userName, String userType, Image userPicture, int[] favoriteExeList) {
        this.userName = userName;
        this.userType = userType;
        this.userPicture = userPicture;
        this.favoriteExeList = favoriteExeList;
    }

    public String getUserName() {
        return userName;
    }

    public String getUserType() {
        return userType;
    }

    public int getUserID() {
        return userID;
    }

    public Image getUserPicture() {
        return userPicture;
    }

    public int[] getFavoriteExeList() {
        return favoriteExeList;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public void setUserType(String userType) {
        this.userType = userType;
    }

    public void setUserPicture(Image userPicture) {
        this.userPicture = userPicture;
    }

    public void setFavoriteExeList(int[] favoriteExeList) {
        this.favoriteExeList = favoriteExeList;
    }


}
