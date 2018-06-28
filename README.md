# Python_Algorithm_Practice. 
----------------------------

    These are some random self-studied codes written in Python 3.

## カバーする予定のアルゴリズム. 
-----------------------------

- [x] 二分探索木(binary tree)   -->   BFS_DFS.py
- [x] グラフの探索(BFS,DFS)      -->   BFS_DFS.py
- [x] 累積和                    -->  comulative_sum.py                             [参照サイト](https://paiza.hatenablog.com/entry/2015/01/21/【累積和、しゃくとり法】初級者でも解るアルゴ "参照サイト") 
- [x] しゃくとり法  
- [ ] 累積xor
- [ ] 二分探索
- [ ] Union-Find
- [ ] 二次元でのいもす法
- [ ] エラストテネスの篩
- [ ] しゃくとり法
- [ ] 二部グラフの最大マッチング(最大流問題)
- [ ] ダイクストラ法
- [ ] 階乗と逆元の前計算による組み合わせの計算
*****
### 各アルゴリズムのポイント

-------------------------

>  * 二分探索木(binary tree). 

       各ノードに左右二本のポインタが付いたデータ構造.  
       定義にもよるが 一般的に、左側にルートの持つ属性値（ex: Int). 
       よりも ”小さい”属性値を持つノードが挿入される.  
       基準となるrootのその値がうまく中央値に近区なければ.   
　　　　また挿入される値にうまくバラつかないと、最悪O(N)になりうる.  



>  * グラフの探索(BFS,DFS). 
  
>  ***Breadth-Fast-Search***. 
     (非再帰的解法）Queue
     
       Queue もしくは　線形のデータ構造で、overrideしてQueueを作る）を使い、ルートをpushした後、子ノード.   
       (left,right)の有無を確認し、存在すればそれらをpushしていく. 


>   ***Depth-Fast-Search***. 
     (非再帰的解法）Stack 

       Stack（もしくは　線形のデータ構造で、overrideしてStackを作る）を使い、ルートをpushした後、子ノード
      （left,right) の有無を確認し、存在すればそれらをpushしていく.     



    
>   * 累積和.  

       一番のメリットは、累積和を使うことで、全探索するよりも高速化する点. 尺取り法とほぼ同様の結果が得られる（とのこと）. 
       O(NlogN) 
       
       
>  * 累積XOR. 


>  * 尺取り法. 

       線形のデータ構造（arrayなど）の中で、かつ、連続する 部分列(subset)を作成したい時に有効. 
       線形の全探索は　O(N^2)に対して、尺取り法はO(N).  
       
       [参考サイト]（https://www.kumilog.net/entry/two-pointers）

       




----------------------------
 


#### References

[Robot Moving](https://www.codechef.com/DEC11/problems/MOVES/ ). 
* mod prime # の理解を深める.

          10億７は素数であり、６４ビットのPCでoverflowしてしまう値を取り扱う時. 
          この素数を % して、　その余り　と　10億７のカウンターなどで扱うこともあるそう。

[Xor Sum](https://beta.atcoder.jp/contests/abc050/tasks/arc066_b ). 
* 
