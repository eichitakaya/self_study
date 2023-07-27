/*
モンテカルロ法を用いて円周率を計算するプログラム．
サンプル数nはコマンドライン引数で指定できるようにする．
*/

// 一様分布乱数を生成するために必要
extern crate rand;
use rand::distributions::{Distribution, Uniform};

fn main() {
    // コマンドライン引数を一つだけ取得しi32型に変換
    let n = std::env::args().nth(1).unwrap().parse::<i32>().unwrap();

    // 円周率を計算
    let pi = calc_pi(n);
}

// 円周率を計算する関数
fn calc_pi(n: i32) -> f64 {
    // 乱数生成器を初期化
    let mut rng = rand::thread_rng();
    let uni = Uniform::from(0.0..1.0);

    // 円周率を計算
    let mut count = 0;
    for _ in 0..n {
        let x = uni.sample(&mut rng);
        let y = uni.sample(&mut rng);
        if x * x + y * y < 1.0 {
            count += 1;
        }
    }
    let pi = 4.0 * (count as f64) / (n as f64);
    println!("pi = {}", pi);
    pi
}
