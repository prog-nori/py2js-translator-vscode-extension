import { Previewer } from './previewer';
import {
	window,
	commands,
	Disposable,
	ExtensionContext,
    workspace,
} from 'vscode';
import { SSL_OP_EPHEMERAL_RSA } from 'constants';

export function activate(context: ExtensionContext) {
    
    console.log('!!!!!!!!!!!!!!!!!! Congratulations, your extension "py2js" is now active!');


    let disposable = commands.registerCommand('py2js.liveConvert', () => {

        const py2jsPreview= new Py2JsPreview(context);
        const controller = new Py2JsPreviewController(py2jsPreview);
        context.subscriptions.push(controller);
        context.subscriptions.push(py2jsPreview);
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {}

export class Py2JsPreview {

	private _context: ExtensionContext;
	private _previewer: Previewer;

	constructor(context: ExtensionContext) {
		this._context = context;
		this._previewer = new Previewer(context);
	}

    public updatePreview() {
        let editor = window.activeTextEditor;
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

    public dispose() {
    }
}

class Py2JsPreviewController {

    private _py2jsPreview: Py2JsPreview;
    private _disposable: Disposable;

    constructor(py2jsPreview: Py2JsPreview) {
        this._py2jsPreview = py2jsPreview;
        // this._py2jsPreview.updatePreview();
        this._onEvent();

        let subscriptions: Disposable[] = [];
        // このイベント、非同期でほぼ常に更新するようにしたら重たいだろうか。
        // ないしは、イベントがあってから数秒以内は非同期で数回更新をかけるようにするとか
        workspace.onDidChangeTextDocument(this._onEvent, this, subscriptions);
        workspace.onDidSaveTextDocument(this._onEvent, this, subscriptions);
        window.onDidChangeTextEditorSelection(this._onEvent, this, subscriptions);
        //
        this._disposable = Disposable.from(...subscriptions);
    }

    private async _onEvent() {
        // イベント発火
        this._py2jsPreview.updatePreview();
        // 発火後0.1秒刻みでイベントを5回(0.5秒間)発火
        let spanedSec = 0;
        const id = setInterval(() => {
            spanedSec++;
            if(spanedSec >= 10) {
                clearInterval(id);
                this._py2jsPreview.updatePreview();
            }
        }, 50);
    }

    public dispose() {
    }
}