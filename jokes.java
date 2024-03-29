import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.http.HttpResponse.BodyHandlers;


public void run(){
  try{ 
    HttpClient client = HttpClient.newHttpClient(); 
    HttpRequest request = HttpRequest.newBuilder()   
     .uri(URI.create("https://icanhazdadjoke.com/")) 
     .header("Accept", "text/plain") // Specify Accept header  
     .GET() 
     .build();   
   String result = client.send(request, BodyHandlers.ofString()).body();      
   System.out.println(result);   
  }     
  catch(Exception e){}
}
