
fn main() {

    let vec1 = vec![1, 2, 3, 4, 5];
    let vec2 = vec![5, 4, 3, 2, 1];

    println!("{}", vec1[0] + vec2[0]);
    println!("{:?}", vec1);
    println!("{:?}", add(vec1, vec2));
    println!("{:?}", vec1);

}

fn add(v1: Vec<i32>, v2: Vec<i32>)  -> Vec<i32>{

    let mut result = Vec::new();
    for i in 0..v1.len() {
        result.push(v1[i] + v2[i]);
    }
    return result
}