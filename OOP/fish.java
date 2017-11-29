 class fish{

    static int no=0;

    static class Fish{

       private static int counter=0;
       private int fin = 4;

       private String priv;
       protected String prot;
       public String pub;


       Fish(){

         priv =  "I am private";
         prot = "I am protected";
         pub = "I am public";
         counter+=1;

       }

       static int getFishInstances(){

         return counter;
       }

       /*Since no destructors in java
          have to call System.gc() manually for it to run*/
       @Override
       public void finalize() {
         System.out.println("Fish has been destroyed");
       }

       public int getFin(){
         return fin;
       }

       public void setFin(int num){
         fin=num;
         return;
       }

       public void delteFin(){
         fin=0;
       }

       public void swim(){
         System.out.println("Swim");
       }

       public void swim_backwards(){
         System.out.println("Back");
       }

       public void skeleton(){
         System.out.println("Skl");
       }
   }

   static class Shark extends Fish{

      private int teeth;

      Shark(int teeth){
        this.teeth = teeth;
      }

      public int getTeeth(){
        return teeth;
      }

   }



   public static void main(String[] args){

     Fish f = new Fish();
     Fish f2 = new Fish();
     System.out.println(f.getFin());
     f2.setFin(9);
     System.out.println(f.getFin());
     System.out.println(f2.getFin());
     System.out.println(Fish.getFishInstances());

     System.out.println(no);

     Shark s1 = new Shark(92);
     System.out.println(s1.getTeeth());
     System.out.println(s1.getFin());


     System.gc();
   }






}
