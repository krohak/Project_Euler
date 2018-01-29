abstract class Employee {
 private Call currentCall = null;
 protected Rank rank;

 public Employee() { }

 /* Start the conversation */
 public void receiveCall(Call call) { ... }

 /* the issue is resolved, finish the call */
 public void callCompleted() { ... }

 /* The issue has not been resolved. Escalate the call, and
 * assign a new call to the employee. */
 public void escalateAndReassign() { ... }


/* Assign a new call to an employee, if the employee is free. */
 public boolean assignNewCall() { ... }

 /* Returns whether or not the employee is free. */
 public boolean isFree() { return currentCall == null; }

 public Rank getRank() { return rank; }
 }


 class Director extends Employee {
public Director() {
rank = Rank.Director;
}
}

class Manager extends Employee {
public Manager() {
rank = Rank.Manager;
}
}

class Respondent extends Employee {
public Respondent() {
rank = Rank.Responder;
}
}
