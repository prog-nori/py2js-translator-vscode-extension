import {
    window as vWindow,
    ViewColumn,
    ExtensionContext,
    WebviewPanel,
    NotebookCellOutput,
} from 'vscode';

import {
    Options,
    PythonShell,
    PythonShellError
} from 'python-shell';

import {
    spawn
} from 'child_process';
import { Readable } from 'stream';

type Response = {
    text: string
    length: number
};

export class Previewer {

    private context_: ExtensionContext;
    private panel_: WebviewPanel;
    private options_: Options;
    private response_: Response;

    constructor(context: ExtensionContext) {
        this.context_ = context;
        this.panel_ = vWindow.createWebviewPanel(
            'preview',
            'プレビュー',
            ViewColumn.One,
            {}
        );
        this.options_ = {
            ...PythonShell.defaultOptions,
            mode: 'text',
            scriptPath: __dirname,
            pythonPath: 'python3'
        };
        this.response_ = {
            text: '',
            length: 0
        };
    }

    private setArg(arg: string, reset: boolean = false) {
        console.log(typeof arg);
        if(Array.isArray(this.options_.args) && reset === false) {
            this.options_.args.push(arg);
        } else {
            this.options_.args = [arg];
        }
    }

    private async run(script: string) {
        const args: Array<string> = this.options_.args? this.options_.args: [];
        const target = `${__dirname}/${script}`;
        const python = spawn('python', [target, args.join(' ')]);
        const chunks: Array<Buffer> = new Array<Buffer>();

        return new Promise((resolve, reject) => {
            python.stdout.on('data', (chunk) => {
                chunks.push(Buffer.from(chunk));
            });
            python.stderr.on('data', (data) => {
                console.error(`stderr: ${data}`);
                reject(data);
            });
            
            python.on('exit', () => {
                resolve(Buffer.concat(chunks).toString('utf-8'));
            });
        });
    }

    public update() {
        let editor = vWindow.activeTextEditor;
        if(editor?.document){
            this.setArg(editor.document.getText(), true);
            // old
            // this.run('translator/execute.py').then(res => {
            this.run('py2js/py2js.py').then(res => {
                console.log('async log:', res);
                this.response_.text = String(res);
            });
        }
        console.log('response:');
        console.log(this.response_);
        this.panel_.webview.html = `<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Cat Coding</title>
        </head>
        <body style="white-space: pre">
            ${this.response_.text}
            <!-- <code style="display: block;white-space: pre-wrap">${this.response_.text}</code> -->
        </body>
        </html>`;
    }
}