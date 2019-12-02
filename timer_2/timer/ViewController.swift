//
//  ViewController.swift
//  timer
//
//  Created by 浅井智博 on 2019/12/02.
//  Copyright © 2019 浅井智博. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    //タイマークラスのインスタンスを生成
    var timer = Timer()
    //count変数に初期値0を代入
    var count = 0
    var minute_count = 0

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    @IBOutlet weak var timer_label: UILabel!
    @IBOutlet weak var minute_timer_label: UILabel!
    
    @IBAction func start_button(_ sender: Any) {
        timer.invalidate()
        timer = Timer.scheduledTimer(timeInterval: 1, target: self, selector:#selector(ViewController.updateTimer),
        userInfo: nil, repeats: true)
    }
    @IBAction func stop_button(_ sender: Any) {
        //invalidateメソッドはオブジェクトからタイマーを削除する
        timer.invalidate()
    }
    @IBAction func reset_botton(_ sender: Any) {
        //invalidateメソッドはオブジェクトからタイマーを削除する
                timer.invalidate()
        //count変数を0にする
                count = 0
                minute_count = 0
        //timerCountLabelのtextプロパティへString型にキャストしたcount変数を代入する（表示させる）
                timer_label.text = String(count)
                minute_timer_label.text = String(minute_count)
        
    }
    //移譲される側のメソッド
    @objc func updateTimer() {
    //countが60に達するまで1ずつ加算されていく
        if count < 59 && minute_count < 10{
        count += 1
    //timerCountLabelのtextプロパティへString型にキャストしたcount変数を代入する（表示させる）
       timer_label.text = String(count)
       minute_timer_label.text = String(minute_count)
    }
        else{
            count = 0
            if minute_count < 10{
            minute_count += 1
            }
            
            timer_label.text = String(count)
            minute_timer_label.text = String(minute_count)
            
        }
        
}
    
    @IBOutlet weak var counter_label: UILabel!
    
    var counter_count = 0
    
    
    @IBAction func counter_plus(_ sender: Any) {
        counter_count += 1
        counter_label.text = String(counter_count)
        
    }
    
    @IBAction func counter_minus(_ sender: Any) {
        if(counter_count > 0){
        counter_count -= 1
        counter_label.text = String(counter_count)
        }
    }
    
    @IBAction func counter_0(_ sender: Any) {
        counter_count = 0
        counter_label.text = String(counter_count)
    }
}
