from ast import Module
class Py2JS:
    def __init__(self: Py2JS, an_abstract_tree: Module) -> None: ...
    def parse(self: Py2JS) -> str:
        """
        デバッグ用。与えられたastを出力。
        """
        pass
    def run(self: Py2JS) -> str: 
        """
        変換機のエントリーポイント。
        変換後の文字列を返す。
        """
        return