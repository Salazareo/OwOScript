import { Server } from '@overnightjs/core';
import { Logger } from '@overnightjs/logger';
import * as bodyParser from 'body-parser';
import * as compression from 'compression';
import * as cookieParser from 'cookie-parser';
import * as express from 'express';
import * as path from 'path';
import Controllers from './controllers';
import { IS_DEV } from './utils/constants';
class StolenServer extends Server {

    private readonly SERVER_START_MSG = 'Stolen server started on port: ';
    private readonly DEV_MSG = 'Express Server is running in development mode. ' +
        'No front-end content is being served.';

    constructor() {
        super(true);
        this.app.use(cookieParser());
        this.app.use(compression());
        this.app.use(bodyParser.json());
        this.app.use(bodyParser.urlencoded({ extended: true }));
        this.setupControllers();
        // if (IS_DEV) {
        //     this.app.get('*', (req, res) => res.send(this.DEV_MSG));
        // } else {

        this.serveFrontEndProd();
        // }
    }

    public start(port: number): void {
        this.app.listen(port, () => {
            Logger.Imp(this.SERVER_START_MSG + port);
        });
    }

    private setupControllers(): void {
        const ctlrInstances = [];
        for (const Controller of Controllers) {
            ctlrInstances.push(new Controller())
        }
        super.addControllers(ctlrInstances);
    }

    private serveFrontEndProd(): void {
        const dir = path.join(__dirname, 'public/');
        this.app.use(express.static(dir));
        this.app.get('*', (req, res) => {
            res.sendFile('index.html', { root: dir });
        });
    }
}

export default StolenServer;