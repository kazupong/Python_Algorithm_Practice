# Python_Algorithm_Practice
These are some random self-studied codes written in Python 3.

## カバーする予定のアルゴリズム
- [x] 二分探索木(binary tree)   -->   BFS_DFS.py
- [x] グラフの探索(BFS,DFS)      -->   BFS_DFS.py
- [x] 累積和                    -->  comulative_sum.py                             [参照サイト](https://paiza.hatenablog.com/entry/2015/01/21/【累積和、しゃくとり法】初級者でも解るアルゴ "参照サイト") 
- [ ] 累積xor
- [ ] 二分探索
- [ ] Union-Find
- [ ] 二次元でのいもす法
- [ ] エラストテネスの篩
- [ ] しゃくとり法
- [ ] 二部グラフの最大マッチング(最大流問題)
- [ ] ダイクストラ法
- [ ] 階乗と逆元の前計算による組み合わせの計算

### 各アルゴリズムのポイント

* 二分探索木(binary tree). 


* グラフの探索(BFS,DFS). 
  -----< Breadth-Fast-Search>. 
    | （非再帰的解法）Queue（もしくは　線形のデータ構造で、overrideしてQueueを作る）を使い、ルートをpushした後、子ノード（left,right). 
    |　　　の有無を確認し、存在すればそれらをpushしていく.  
    |--< Depth-Fast-Search >. 
    |   （非再帰的解法）Stack（もしくは　線形のデータ構造で、overrideしてStackを作る）を使い、ルートをpushした後、子ノード（left,right）. 
    |　　　の有無を確認し、存在すればそれらをpushしていく.  

* 累積和.  
    |-- 一番のメリットは、累積和を使うことで、全探索するよりも高速化する点. 
  


#### References

[Robot Moving](https://www.codechef.com/DEC11/problems/MOVES/ ). 
* mod prime # の理解を深める. 

[Xor Sum](https://beta.atcoder.jp/contests/abc050/tasks/arc066_b ). 
* 
