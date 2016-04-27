#include<stdio.h>
#include<omp.h>

void comput(float* A, float* B, float* C) //两个矩阵相乘传统方法
{
    int x, y;
    for(y = 0; y < 4; y++) {
        for(x = 0; x < 4; x++) {
            C[4 * y + x] = A[4 * y + 0] * B[4 * 0 + x] + A[4 * y + 1] * B[4 * 1 + x] +
                           A[4 * y + 2] * B[4 * 2 + x] + A[4 * y + 3] * B[4 * 3 + x];
        }
    }
}

int main()
{
    double duration;
    double s, f;
    int x = 0;
    int y = 0;
    int n = 0;
    int k = 0;
    float A[] = {1, 2, 3, 4,
                 5, 6, 7, 8,
                 9, 10, 11, 12,
                 13, 14, 15, 16
                };
    float B[] = {0.1f, 0.2f, 0.3f, 0.4f,
                 0.5f, 0.6f, 0.7f, 0.8f,
                 0.9f, 0.10f, 0.11f, 0.12f,
                 0.13f, 0.14f, 0.15f, 0.16f
                };

    float C[16];

    s = omp_get_wtime();

    //#pragma omp parallel if(false)
    for(n = 0; n < 1000000; n++) {
        comput(A, B, C);
    }
    f = omp_get_wtime();
    duration = f - s;
    printf("s---1,000,000 :%f\n", duration);
    for(y = 0; y < 4; y++) {
        for(x = 0; x < 4; x++) {
            printf("%f,", C[y * 4 + x]);
        }
        printf("\n");
    }

    printf("\n======================\n");
    s = omp_get_wtime();
    //parallel 2
    #pragma omp parallel for
    for(n = 0; n < 2; n++) { ////CPU是核线程的
        for(k = 0; k < 500000; k++) { //每个线程管个循环
            comput(A, B, C);
        }
    }
    f = omp_get_wtime();
    duration = f - s;
    printf("p2- 1,000,000:%f\n", duration);


    //parallel 3
    s = omp_get_wtime();
    #pragma omp parallel for
    for(n = 0; n < 4; n++) {	//CPU是核线程的
        for(k = 0; k < 250000; k++) { //每个线程管个循环
            comput(A, B, C);
        }
    }
    f = omp_get_wtime();
    duration = f - s;

    printf("p3- 1,000,000:%f\n", duration);


    //parallel 1
    s = omp_get_wtime();
    #pragma omp parallel for
    for(n = 0; n < 1000000; n++) {
        comput(A, B, C);
    }
    f = omp_get_wtime();
    duration = f - s;

    printf("p1-  1,000,000 :%f\n", duration);



    for(y = 0; y < 4; y++) {
        for(x = 0; x < 4; x++) {
            printf("%f,", C[y * 4 + x]);
        }
        printf("\n");
    }

    return 0;
}
