#include <iostream>

#include <thread>
using namespace std;

void fun_1() {
    while (1) {
        cout << "Ahmed" << endl;
    }
}
void fun_2() {
    while (1) {
        cout << "Mohamed" << endl;
    }
}

int main() {
    cout << "Hello world" << endl;
    thread f1(fun_1);
    thread f2(fun_2);
    f1.join();
    f2.join();

    return 0;
}