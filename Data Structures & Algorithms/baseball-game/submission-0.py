class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for op in operations:
            if op == 'C':
                record.pop()
            elif op == 'D':
                val = record[-1] * 2
                record.append(val)
            elif op == "+":
                val = record[-1] + record[-2]
                record.append(val)
            else:
                record.append(int(op))

        return sum(record)
