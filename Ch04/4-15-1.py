import scipy.special
import numpy


# 신경망 클래스의 정의
class neuralNetwork:

    # 신경망 초기화 (입력노드 , 은닉노드 , 출력 노드 , 학습률)
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # 입력, 은닉, 출력 계층의 노드 개수 설정
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        # 가중치 행렬 wih 와 who
        # self.wih = (numpy.random.rand(self.hnodes, self.inodes)-0.5)
        # self.who = (numpy.random.rand(self.onodes, self.hnodes)-0.5)

        # 더 정교한 가중치
        self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))

        # 학습률
        self.lr = learningrate

        # 활성화 함수로는 시그모이드 함수를 이용
        self.activation_function = lambda x: scipy.special.expit(x)

    # 신경망 학습
    def train(self, input_list, targets_list):
        # 입력 리스트를 2차원 행렬로 변환
        inputs = numpy.array(input_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        # 은닉 계층으로 들어오는 신호를 계산
        hidden_inputs = numpy.dot(self.wih, inputs)
        # 은닉 계층으로 나가는 신호를 계산
        hidden_outputs = self.activation_function(hidden_inputs)
        # 최종 출력 계층으로 들어오는 신호를 계산
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # 최종 출력 계층으로 나가는 신호를 계산
        final_outputs = self.activation_function(final_inputs)

        # 출력계층의 오차는 (실제 값 - 계산 값)
        output_errors = targets - final_outputs
        # 은닉 계층의 오차는 가중치에 의해 나뉜 출력 계층의 오차들을 재조합해 계산
        hidden_errors = numpy.dot(self.who.T, output_errors)

        # 은닉 계층과 출력 계층 간의 가중치 업데이트
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)),
                                        numpy.transpose(hidden_outputs))
        # 입력 계층과 은닉 계층간의 가중치 업데이트
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)),
                                        numpy.transpose(inputs))

    # 신경망에 질의
    def query(self, inputs_list):
        # 입력 리스트를 2차원 행렬로 변환
        inputs = numpy.array(inputs_list, ndmin=2).T

        # 은닉 계층으로 들어오는 신호를 계산
        hidden_inputs = numpy.dot(self.wih, inputs)

        # 은닉 계층으로 나가는 신호를 계산
        hidden_outputs = self.activation_function(hidden_inputs)

        # 최종 출력 계층으로 들어오는 신호를 계산
        final_inputs = numpy.dot(self.who, hidden_outputs)

        # 최종 출력 계층에서 나가는 신호를 계산
        final_outputs = self.activation_function(final_inputs)

        return final_outputs


if __name__ == '__main__':
    # 입력, 은닉, 출력 노드의 수
    input_nodes = 2
    hidden_nodes = 2
    output_nodes = 1

    # 학습률 0.3
    learning_rate = 0.01

    # 학습횟수
    epochs = 1000000

    # 인스턴스 생성
    n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

    #학습하기
    for i in range(epochs):
        n.train([0, 0], [0])
        n.train([0, 1], [1])
        n.train([1, 0], [1])
        n.train([1, 1], [0])
        print('학습횟수 : ', i)

    #검증하기
    print('XOR 결과')
    print('0, 0 : ', n.query([0, 0]))
    print('0, 1 : ', n.query([0, 1]))
    print('1, 0 : ', n.query([1, 0]))
    print('1, 1 : ', n.query([1, 1]))