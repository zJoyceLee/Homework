
CPU Affinity
============

An example about CPU Affinity.

This example shows how to set cpu for threads.

This used 'while(1);', so the CPU will display 100% used.

----
How to compile main.cpp:

    gcc main.cpp -o main

Run by: 

    ./main

Then turn on a termial to run 'htop' or 'top':

    htop

How to change CPU mask for program:

    sed -e 's/active_cpu = 0/active_cpu = 1/' main.cpp > main_1.cpp

You can show the difference between main.cpp and main_1.cpp by:

     diff  main.cpp main_1.cpp

It might display like this:

    52c52
    <        uint32_t active_cpu = 0;
    ---
    >        uint32_t active_cpu = 1;

Then you should compile main_1.cpp the same way:

    gcc main_1.cpp -o main_1

You can see the effect by htop too.
