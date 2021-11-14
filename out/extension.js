"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.Py2JsPreview = exports.deactivate = exports.activate = void 0;
const previewer_1 = require("./previewer");
const vscode_1 = require("vscode");
function activate(context) {
    console.log('!!!!!!!!!!!!!!!!!! Congratulations, your extension "py2js" is now active!');
    let disposable = vscode_1.commands.registerCommand('py2js.liveConvert', () => {
        const py2jsPreview = new Py2JsPreview(context);
        const controller = new Py2JsPreviewController(py2jsPreview);
        context.subscriptions.push(controller);
        context.subscriptions.push(py2jsPreview);
    });
    context.subscriptions.push(disposable);
}
exports.activate = activate;
function deactivate() { }
exports.deactivate = deactivate;
class Py2JsPreview {
    constructor(context) {
        this._context = context;
        this._previewer = new previewer_1.Previewer(context);
    }
    updatePreview() {
        let editor = vscode_1.window.activeTextEditor;
        if (!editor) {
            return;
        }
        console.log('==================================================');
        // 入力の度に以下の行が実行される。
        this._previewer.update();
        // previewer(this._context);
        // 未実装(必須): python 以外のコードを省く
        // let doc = editor.document;
        // console.log(doc.uri.path);
        // console.log(doc.uri.scheme);
        // console.log(doc.languageId);
        // console.log(doc.getText());
    }
    dispose() {
    }
}
exports.Py2JsPreview = Py2JsPreview;
class Py2JsPreviewController {
    constructor(py2jsPreview) {
        this._py2jsPreview = py2jsPreview;
        // this._py2jsPreview.updatePreview();
        this._onEvent();
        let subscriptions = [];
        // このイベント、非同期でほぼ常に更新するようにしたら重たいだろうか。
        // ないしは、イベントがあってから数秒以内は非同期で数回更新をかけるようにするとか
        vscode_1.workspace.onDidChangeTextDocument(this._onEvent, this, subscriptions);
        vscode_1.workspace.onDidSaveTextDocument(this._onEvent, this, subscriptions);
        vscode_1.window.onDidChangeTextEditorSelection(this._onEvent, this, subscriptions);
        //
        this._disposable = vscode_1.Disposable.from(...subscriptions);
    }
    _onEvent() {
        return __awaiter(this, void 0, void 0, function* () {
            // イベント発火
            this._py2jsPreview.updatePreview();
            // 発火後0.1秒刻みでイベントを5回(0.5秒間)発火
            let spanedSec = 0;
            const id = setInterval(() => {
                spanedSec++;
                if (spanedSec >= 10) {
                    clearInterval(id);
                    this._py2jsPreview.updatePreview();
                }
            }, 50);
        });
    }
    dispose() {
    }
}
//# sourceMappingURL=extension.js.map