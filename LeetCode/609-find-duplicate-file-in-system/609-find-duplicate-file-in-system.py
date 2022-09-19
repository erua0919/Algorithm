from collections import defaultdict
class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        _dict=defaultdict(list)
        for path in paths:
            path=path.split()
            root=path[0]
            for _file in path[1:]:
                root2,content=_file.split('(')
                _dict[content[:-1]].append(root+'/'+root2)
        return [value for value in _dict.values() if len(value)>1]
        