package com.example.panchy.virtualgym.ModelClass;

import android.media.Image;

/**
 * Created by Panchy on 2017/9/28.
 */

public class Moderator extends User {

    public Moderator(String userName, String userType, Image userPicture, int[] favoriteExeList) {
        super(userName, userType, userPicture, favoriteExeList);
    }
}
