bool has_cycle(Node* head) {

    if (head == NULL){
        return 0;
    }

    Node *ptr1 = head;
    Node *ptr2 = head;

    while(ptr1 != NULL && ptr2 != NULL && ptr1->next){

        ptr1 = ptr1->next->next;
        ptr2 = ptr2->next;

        if(ptr1==ptr2){
            return 1;
        }

    }

    return 0;
}



/*
bool has_cycle(Node* head) {
    if (head == NULL){
        return 0;
    }
    Node* node1 = head;
    Node* node2 = head;
    node2 = node2->next;
    while((node1->data != node2->data) && (node1 != NULL) && (node2 != NULL)){
        node1 = node1->next;
        node2 = node2->next->next;
    }
    if(node1 == NULL || node2 == NULL){
        return 0;
    }

    return 1;
}
/*
