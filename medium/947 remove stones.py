class Solution:
     def removeStones(self, points):
        UF = {}
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)

        for i, j in points:
            union(i, ~j)
        return len(points) - len({find(x) for x in UF})

"""
1. Connected stones
Two stones are connected if they are in the same row or same col.
Connected stones will build a connected graph.
It's obvious that in one connected graph,
we can't remove all stones.

We have to have one stone left.
An intuition is that, in the best strategy, we can remove until 1 stone.

I guess you may reach this step when solving the problem.
But the important question is, how?


2. A failed strategy
Try to remove the least degree stone
Like a tree, we try to remove leaves first.
Some new leaf generated.
We continue this process until the root node left.

However, there can be no leaf.
When you try to remove the least in-degree stone,
it won't work on this "8" like graph:
[[1, 1, 0, 0, 0],
[1, 1, 0, 0, 0],
[0, 1, 1, 0, 0],
[0, 0, 1, 1, 1],
[0, 0, 0, 1, 1]]

The stone in the center has least degree = 2.
But if you remove this stone first,
the whole connected stones split into 2 parts,
and you will finish with 2 stones left.


3. A good strategy
In fact, the proof is really straightforward.
You probably apply a DFS, from one stone to next connected stone.
You can remove stones in reversed order.
In this way, all stones can be removed but the stone that you start your DFS.

One more step of explanation:
In the view of DFS, a graph is explored in the structure of a tree.
As we discussed previously,
a tree can be removed in topological order,
from leaves to root.


4. Count the number of islands
We call a connected graph as an island.
One island must have at least one stone left.
The maximum stones can be removed = stones number - islands number

The whole problem is transferred to:
What is the number of islands?

You can show all your skills on a DFS implementation,
and solve this problem as a normal one.


5. Unify index
Struggle between rows and cols?
You may duplicate your codes when you try to the same thing on rows and cols.
In fact, no logical difference between col index and rows index.

An easy trick is that, add 10000 to col index.
So we use 0 ~ 9999 for row index and 10000 ~ 19999 for col.


6. Search on the index, not the points
When we search on points,
we alternately change our view on a row and on a col.

We think:
a row index, connect two stones on this row
a col index, connect two stones on this col.

In another view：
A stone, connect a row index and col.

Have this idea in mind, the solution can be much simpler.
The number of islands of points,
is the same as the number of islands of indexes.


7. Union-Find
I use union find to solve this problem.
As I mentioned, the elements are not the points, but the indexes.

for each point, union two indexes.
return points number - union number
Copy a template of union-find,
write 2 lines above,
you can solve this problem in several minutes.


Complexity
union and find functions have worst case O(N), amortize O(1)
The whole union-find solution with path compression,
has O(N) Time, O(N) Space
"""