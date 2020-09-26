package ToolsQA;

import ToolsQA.models.Request;
import ToolsQA.models.Response;
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;

public class Handler implements RequestHandler<Request, Response> {

    public Response handleRequest(Request input, Context context) {
        Calculadora calculadora = new Calculadora();
        Integer result;

        if (input.getMethod().equals("add")){
            result = calculadora.addNumbers(input.getA(), input.getB());
        }
        else if (input.getMethod().equals("sub")){
            result = calculadora.addNumbers(input.getA(), input.getB());
        }
        else if (input.getMethod().equals("multi")){
            result = calculadora.addNumbers(input.getA(), input.getB());
        } else {
            result = 0;
            return new Response(result,"404");
        }

        return new Response(result,"200");
    }
}
