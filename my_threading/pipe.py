# from multiprocessing import Process, Pipe
#
#
# def f(conn):
#     conn.send([42, None, 'hello'])
#     conn.close()
#
#
# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()
#     p = Process(target=f, args=(child_conn,))
#     p.start()
#     print(parent_conn.recv())   # prints "[42, None, 'hello']"
#     p.join()
#
#
# for i in range(100):
#     print(i)
#     if i == 70:
#         break
# else:
#     print('terminé')


if None:
    print('cool')