#include <iostream>
#include <bits/stdc++.h>
#include <conio.h>
#define ROW 5
#define coloum 5
using namespace std;

struct chamb
{
	int x;
	int y;
};

struct queuex
{
	chamb pt;
	int distance;
};

bool checkValid(int r, int c)
{
	return ((r >= 0) && (r < ROW) &&	(c >= 0) && (c < coloum));
}

int rNum[] = {-1, 1, 2, 1};
int cNum[] = {0, -1, 0, 0};

int Lee(int matrix[][coloum], chamb source, chamb destination)
{
	if (!matrix[source.x][source.y] || !matrix[destination.x][destination.y])
		return -1;

	bool visited[ROW][coloum];
	memset(visited, false, sizeof visited);

	visited[source.x][source.y] = true;

	queue<queuex> q;

	queuex s = {source, 0};
	q.push(s);

	while (!q.empty())
	{
		queuex curr = q.front();
		chamb pt = curr.pt;

		if (pt.x == destination.x && pt.y == destination.y)
			return curr.distance;
		q.pop();
		for (int i = 0; i < 4; i++)
		{
			int r = pt.x + rNum[i];
			int c = pt.y + cNum[i];

			if (checkValid(r, c) && matrix[r][c] &&
			!visited[r][c])
			{

				visited[r][c] = true;
				queuex Adjcell = { {r, c},curr.distance+ 1 };
				q.push(Adjcell);
			}
		}
	}

	return -1;
}

int main()
{
	int matrix[ROW][coloum] =
	{
		{ 0, 0, 1, 1, 0 },
		{ 1, 0, 1, 0, 1 },
		{ 1, 1, 0, 1, 0 },
		{ 0, 0, 0, 0, 1 },
		{ 1, 1, 1, 1, 0 }};

	chamb source = {0, 0};
	chamb destination = {1, 1};

	int distance = Lee(matrix, source, destination);

	if (distance != -1)
		cout<< "Length of the Shortest Path is "<<distance ;
	else
		cout<< "Shortest Path doesn't exist";

	return 0;
}

