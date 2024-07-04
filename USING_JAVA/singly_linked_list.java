import java.util.*;
//NOT_> for each class ,,after compile .class file is created
import java.util.*;
 class Node{
    public int data;
    public Node next;
    public Node(int data,Node next){
        this.data=data;
        this.next=next;
    }
}

 class ll{
    public Node head;
    public ll(){
        this.head=null;
    }
    public void insert_at_begining(int data){
        Node node=new Node(data,this.head);
        this.head=node;
    }
    public void print(){
       Node  itr=this.head;
       String listr="";
       while (itr != null){
        listr+=String.valueOf(itr.data);//type casting
        if (itr.next != null){
            listr+="-->";
        }
        itr=itr.next;
       }
       System.out.println(listr);
    }
}
public class singly_linked_list{
    public static void main(String args[]){
        ll a=new ll();
        a.insert_at_begining(5);
        a.insert_at_begining(10);
        a.print();
    }
}