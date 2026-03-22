import { Router, type IRouter } from "express";
import healthRouter from "./health";
import parseTreatRouter from "./parse-treat";

const router: IRouter = Router();

router.use(healthRouter);
router.use(parseTreatRouter);

export default router;
