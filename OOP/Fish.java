class Fish{

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

       @Override
       public int hashCode(){
         final int prime =31;
         int result =1;

         result = prime*result+fin;
         return result;

       }

       @Override
       public boolean equals(Object obj){

         if(this == obj)
            return true;
         if(obj == null)
            return false;
         if(getClass() != obj.getClass())
           return false;

         Fish other = (Fish) obj;
         if (fin == 0){
           if(other.fin != 0)
            return false;
         }
         else if(fin != (other.fin))
            return false;
         return true;
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
