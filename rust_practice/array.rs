fn main() {
    let v1 = vec![vec![1, 2, 3, 4, 5], vec![5, 4, 3, 2, 1]];
    let a = NdArray { arr:v1 };
    println!("{:?}", a.sum());

}


#[derive(Debug)]
struct NdArray {
    //nd: u32,
    //shape: Vec<i32>,
    arr: Vec<i64>
}

impl NdArray {
    fn sum(&self) -> i64 {
        let mut result: i64 = 0;
        for i in 0..self.arr.len() {
            result += self.arr[i];
        }
        return result
    }
}