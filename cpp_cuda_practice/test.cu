#include <stdio.h>
#include <stdlib.h>
 
#define N 1000000
 
__global__ void add(int *a, int *b, int*c)
{
	int tid = threadIdx.x + blockIdx.x * blockDim.x;
	while (tid < N)
	{
		c[tid] = a[tid] + b[tid];
		tid += blockDim.x * gridDim.x;
	}
}
 
int main(void)
{
	int *a, *b, *c;
	int *dev_a, *dev_b, *dev_c;
 
	// CPU側でメモリを割り当てる
	a = (int *)malloc(N * sizeof(int));
	b = (int *)malloc(N * sizeof(int));
	c = (int *)malloc(N * sizeof(int));
 
	// GPU側でメモリを割り当てる
	cudaMalloc((void**)&dev_a, N * sizeof(int));
	cudaMalloc((void**)&dev_b, N * sizeof(int));
	cudaMalloc((void**)&dev_c, N * sizeof(int));
 
	// CPU側で配列aと配列bを設定する
	for (int i = 0; i < N; i++)
	{
		a[i] = i;
		b[i] = 2 * i;
	}
 
	// 配列aと配列bをGPUにコピーする
	cudaMemcpy(dev_a, a, N * sizeof(int), cudaMemcpyHostToDevice);
	cudaMemcpy(dev_b, b, N * sizeof(int), cudaMemcpyHostToDevice);
 
	add << <128, 128 >> >(dev_a, dev_b, dev_c);
 
	// 配列cをGPUからCPUにコピーする
	cudaMemcpy(c, dev_c, N * sizeof(int), cudaMemcpyDeviceToHost);
 
	// 要求した処理をGPUが行ったことを確認する
	bool success = true;
	for (int i = 0; i < N; i++)
	{
		if ((a[i] + b[i]) != c[i])
		{
			printf("Error: %d + %d != %d\n", a[i], b[i], c[i]);
			success = false;
		}
	}
	if (success)
	{
		printf("We did it !\n");
	}
 
	// GPU側で割り当てたメモリを開放する
	cudaFree(dev_a);
	cudaFree(dev_b);
	cudaFree(dev_c);
 
	// CPU側で割り当てたメモリを解放する
	free(a);
	free(b);
	free(c);
 
	int i;
	scanf("%d", &i);
 
	return 0;
}