#pragma once

#include <iostream>
#include <thread>

using namespace std;

class SERIAL{

    public:
        static void init();
        static void Read();
        static void Send();

    private:
        bool once;
        

};
