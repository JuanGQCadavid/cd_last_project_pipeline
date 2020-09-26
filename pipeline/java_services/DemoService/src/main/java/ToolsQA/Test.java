package ToolsQA;

import ToolsQA.models.Request;

public class Test {
    public static void main(String[] args) {
        Handler handler = new Handler();

        System.out.println(handler.handleRequest(new Request(5,5,"sdf"), null));
    }
}
