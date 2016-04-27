#include <cstdio>

int main()
{
    # pragma omp parallel for
    for(auto i = 0; i < 12; ++i) {
        printf("This is 'i': %d.\n", i);
    }
    return 0;
}
