import { Controller, Post } from '@overnightjs/core';
import { Logger } from '@overnightjs/logger';
import { execSync } from 'child_process';
import { createHash } from 'crypto';
import { Request, Response } from 'express';
import * as fs from 'fs';
import { StatusCodes } from 'http-status-codes';
@Controller('api/compile')
class CompilerController {

    @Post()
    public compileCode(req: Request, res: Response) {
        try {
            const { code } = req.body;
            const hashName = createHash('md5').update(code).digest('hex');
            if (fs.existsSync(`./${hashName}.js`)) {
                const compiledCode: string = fs.readFileSync(`./${hashName}.js`).toString().trim().replace('\r', '');
                return res.status(StatusCodes.OK).json({
                    compiledCode,
                });
            } else {
                fs.writeFileSync(`./${hashName}.owo`, code);
                const output: string = execSync(`python ../parser.py ./${hashName}.owo`).toString().trim().replace('\r', '');
                // execSync(`rm ./${hashName}.owo`);
                if (!output.endsWith('parsing complete')) {
                    throw Error(output)
                }
                const jsOutput: string = execSync(`python ../toJS.py ./${hashName}.owo.json`).toString().trim().replace('\r', '');
                // execSync(`rm ./${hashName}.owo.json`); // <- if we want this comment it out
                if (!jsOutput.endsWith('compiling complete')) {
                    throw Error(output)
                }
                const compiledCode: string = fs.readFileSync(`./${hashName}.js`).toString().trim().replace('\r', '');
                res.status(StatusCodes.OK).json({
                    compiledCode,
                });
                // execSync(`rm ./${hashName}.js`);
            }
        } catch (err) {
            Logger.Err(err, true);
            return res.status(StatusCodes.BAD_REQUEST).json({
                error: err.message,
            });
        }
    }
}

export default CompilerController;