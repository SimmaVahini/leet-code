function combinationSum(candidates: number[], target: number): number[][] {
    const result: number[][] = [];

    function backtrack(start: number, current: number[], remaining: number) {
        if (remaining === 0) {
            result.push([...current]);
            return;
        }

        if (remaining < 0) return;

        for (let i = start; i < candidates.length; i++) {
            current.push(candidates[i]);
            backtrack(i, current, remaining - candidates[i]); 
            current.pop();
        }
    }

    backtrack(0, [], target);
    return result;
}
