import java.util.HashMap;

 class datastructsmap{

   public static void main(String[] args){

     HashMap<String, Integer> colors = new HashMap<String, Integer>();

     colors.put("Red",1);
     colors.put("Blue",55);
     System.out.println(colors);

     System.out.println(colors.containsKey("Red"));
     System.out.println(colors.containsValue(1));
     System.out.println(colors.size());


     try{
            colors.get(1);
            System.out.println(colors);
     }
     catch(Exception e){
       System.out.println("what");
     }

     /*for(String s, Integer i: colors){
       System.out.println(s);
     }*/

     colors.clear();
     System.out.println(colors);


   }

}
