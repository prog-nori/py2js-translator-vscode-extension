import { Previewer } from './previewer';
import {
	window,
	commands,
	Disposable,
	ExtensionContext,
} from 'vscode';

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
        this._py2jsPreview.updatePreview();

        let subscriptions: Disposable[] = [];
        window.onDidChangeTextEditorSelection(this._onEvent, this, subscriptions);
        this._disposable = Disposable.from(...subscriptions);
    }

    private _onEvent() {
        this._py2jsPreview.updatePreview();
    }

    public dispose() {
    }
}