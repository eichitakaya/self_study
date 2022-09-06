fn main() {
    println!("Hello, world!");
}

// 2つのベクトルの内積を計算する関数
fn dot1d(v1: Vec<f64> , v2: Vec<f64> )  -> f64 {
    //v1とv2の次元が揃っているかチェック
    let mut sum: f64 = 0.0;
    for i in 0 .. v1.len() {
        sum += v1[i] * v2[i];
    }
    sum
}

#[test]
fn test_dot1d() {
    let v1: Vec<f64> = vec![1.0, 2.0, 3.0];
    let v2: Vec<f64> = vec![1.0, 2.0, 3.0];
    let result1: f64 = dot1d(v1, v2);
    
    assert_eq!(result1, 14.0);

    

    assert_eq!(dot1d(v3, v3), 15);
}

fn dot2d(m1: Vec<Vec<f64>>, m2: Vec<Vec<f64>>) -> Vec<Vec<f64>> {
    let v3 = vec![vec![1.0, 2.0, 3.0], vec![3.0, 2.0, 1.0]];
    v3
}

fn test_dot2d() {
    let v1: Vec<f64> = vec![1.0, 2.0, 3.0];
    let v2: Vec<f64> = vec![1.0, 2.0, 3.0];
    let result1: f64 = dot1d(v1, v2);

    let mut v3 = Vec::new();
    v3.push(v1);
    v3.push(v2);

    let result2: f64 = dot1d(v3, v3);
    
    assert_eq!(result1, 14.0);
    assert_eq!(result2, 14.0);
}


