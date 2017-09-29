package com.example.panchy.virtualgym;

import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;

import com.example.panchy.virtualgym.ModelClass.Exercise;
import com.example.panchy.virtualgym.ModelClass.User;

import java.util.ArrayList;

public class SearchActivity extends AppCompatActivity {

    private ArrayList<Exercise> arrayList;
    private User user;
    private Exercise exercise;
    ExerciseController exerciseController=new ExerciseController();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_search);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });
    }

    public Exercise searchBy(User u,Exercise e){
        exercise=exerciseController.fliterBy(u,e);
        return exercise;

    }



}
