from numpy import array

motifs = []
nb_motifs = 11

motifs.append(array([array([1,1,1]),array([0,0,0]),array([1,1,1])])) #couloir v1 27%
motifs.append(array([array([1,0,1]),array([1,0,1]),array([1,0,1])])) #couloir v2 27%
motifs.append(array([array([1,0,1]),array([0,0,0]),array([1,1,1])])) #intersection v1 37%
motifs.append(array([array([1,0,1]),array([0,0,1]),array([1,0,1])])) #intersection v2 37%
motifs.append(array([array([1,1,1]),array([0,0,0]),array([1,0,1])])) #intersection v3 37%
motifs.append(array([array([1,0,1]),array([1,0,0]),array([1,0,1])])) #intersection v4 37%
#motifs.append(array([array([1,0,1]),array([0,0,0]),array([1,0,1])])) #carrefour 0%
motifs.append(array([array([1,0,1]),array([0,0,1]),array([1,1,1])])) #virage v1 37%
motifs.append(array([array([1,1,1]),array([0,0,1]),array([1,0,1])])) #virage v2 37%
motifs.append(array([array([1,1,1]),array([1,0,0]),array([1,0,1])])) #virage v3 37%
motifs.append(array([array([1,0,1]),array([1,0,0]),array([1,1,1])])) #virage v4 37%
motifs.append(array([array([1,1,1]),array([1,1,1]),array([1,1,1])])) #mur 0%